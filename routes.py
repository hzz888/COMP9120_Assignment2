# Importing the frameworks

from flask import *
from datetime import datetime
import database

user_details = {}
session = {}
page = {}

# Initialise the application
app = Flask(__name__)
app.secret_key = 'aab12124d346928d14710610f'


#####################################################
##  INDEX
#####################################################

@app.route('/')
def index():
    # Check if the user is logged in
    if('logged_in' not in session or not session['logged_in']):
        return redirect(url_for('login'))
    page['title'] = 'SharePlus Online Trading'
    
    return redirect(url_for('list_instruction'))

    #return render_template('index.html', session=session, page=page, user=user_details)

#####################################################
##  LOGIN
#####################################################

@app.route('/login', methods=['POST', 'GET'])
def login():
    # Check if they are submitting details, or they are just logging in
    if (request.method == 'POST'):
        # submitting details
        login_return_data = check_login(request.form['id'], request.form['password'])

        # If they have incorrect details
        if login_return_data is None:
            page['bar'] = False
            flash("Incorrect login info, please try again.")
            return redirect(url_for('login'))

        # Log them in
        page['bar'] = True
        welcomestr = 'Welcome back, ' + login_return_data['firstname'] + ' ' + login_return_data['lastname']
        flash(welcomestr)
        session['logged_in'] = True

        # Store the user details
        global user_details
        user_details = login_return_data
        return redirect(url_for('index'))

    elif (request.method == 'GET'):
        return(render_template('login.html', page=page))

#####################################################
##  LOGOUT
#####################################################

@app.route('/logout')
def logout():
    session['logged_in'] = False
    page['bar'] = True
    flash('You have been logged out. See you soon!')
    return redirect(url_for('index'))

#####################################################
##  LIST INSTRUCTION
#####################################################

@app.route('/list_instruction', methods=['POST', 'GET'])
def list_instruction():
    # Check if user is logged in
    if ('logged_in' not in session or not session['logged_in']):
        return redirect(url_for('login'))

    # User is just viewing the page
    if (request.method == 'GET'):
        # First check if specific instruction
        instruction_list = database.findInstructionsByAdm(user_details['login'])
        if (instruction_list is None):
            instruction_list = []
            flash("There are no instructions in the system for " + user_details['firstname'] + " " + user_details['lastname'])
            page['bar'] = False
        return render_template('instruction_list.html', instruction=instruction_list, session=session, page=page)

    # Otherwise try to get from the database
    elif (request.method == 'POST'):
        search_term = request.form['search']
        if (search_term == ''):
            instruction_list_find = database.findInstructionsByAdm(user_details['login'])
        else:    
            instruction_list_find = database.findInstructionsByCriteria(search_term)
        if (instruction_list_find is None):
            instruction_list_find = []
            flash("Searching \'{}\' does not return any result".format(request.form['search']))
            page['bar'] = False
        return render_template('instruction_list.html', instruction=instruction_list_find, session=session, page=page)

#####################################################
##  Add Instruction
#####################################################

@app.route('/new_instruction' , methods=['GET', 'POST'])
def new_instruction():
    # Check if the user is logged in
    if ('logged_in' not in session or not session['logged_in']):
        return redirect(url_for('login'))

    # If we're just looking at the 'new instruction' page
    if(request.method == 'GET'):
        times = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        return render_template('new_instruction.html', user=user_details, times=times, session=session, page=page)

	# If we're adding a new instruction
    success = database.addInstruction(request.form['amount'],
                                 request.form['frequency'],
                                 request.form['customer'],
                                 user_details['login'],
                                 request.form['etf'],
                                 request.form['notes'])
    if(success == True):
        page['bar'] = True
        flash("Instruction added!")
        return(redirect(url_for('index')))
    else:
        page['bar'] = False
        flash("There was an error adding a new instruction")
        return(redirect(url_for('new_instruction')))

#####################################################
## Update Instruction
#####################################################
@app.route('/update_instruction', methods=['GET', 'POST'])
def update_instruction():
    # Check if the user is logged in
    if ('logged_in' not in session or not session['logged_in']):
        return redirect(url_for('login'))

    # If we're just looking at the 'update instruction' page
    if (request.method == 'GET'):
        # Get the instruction
        instruction = {
            'instruction_id': request.args.get('instruction_id'),
            'amount': request.args.get('amount'),
            'frequency': request.args.get('frequency'),
            'expirydate': datetime.strptime(request.args.get('expirydate'), '%d-%m-%Y').date(),
            'customer': request.args.get('customer'),
            'etf': request.args.get('etf'),
            'notes': request.args.get('notes')
        }

        # If there is no instruction
        if instruction['instruction_id'] is None:
            instruction = []
		    # Do not allow viewing if there is no instruction to update
            page['bar'] = False
            flash("You do not have access to update that record!")
            return(redirect(url_for('index')))

	    # Otherwise, if instruction details can be retrieved
        times = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        return render_template('update_instruction.html', instructionInfo=instruction, user=user_details, times=times, session=session, page=page)

    # If we're updating instruction
    success = database.updateInstruction(request.form['instruction_id'],
                                request.form['amount'],
                                request.form['frequency'],
                                request.form['expirydate'],
                                request.form['customer'],
                                user_details['login'],
                                request.form['etf'],
                                request.form['notes'])
    if (success == True):
        page['bar'] = True
        flash("Instruction record updated!")
        return(redirect(url_for('index')))
    else:
        page['bar'] = False
        flash("There was an error updating the instruction")
        return(redirect(url_for('index')))

def get_instruction(instruction_id, username):
    for instruction in database.findInstructionsByAdm(username):
        if instruction['instruction_id'] == instruction_id:
            return instruction
    return None

def check_login(username, password):
    userInfo = database.checkAdmCredentials(username, password)

    if userInfo is None:
        return None
    else:
        tuples = {
            'login': userInfo[0],
            'password': userInfo[1],
            'firstname': userInfo[2],
            'lastname': userInfo[3],
            'email': userInfo[4],
            'remuneration': userInfo[5],
        }
        return tuples
