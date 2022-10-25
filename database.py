#!/usr/bin/env python3
import psycopg2

#####################################################
##  Database Connection
#####################################################

'''
Connect to the database using the connection string
'''
def openConnection():
    # connection parameters - ENTER YOUR LOGIN AND PASSWORD HERE
    userid = "y22s2c9120_zhuo9903"
    passwd = "qK4TdzhQ"
    myHost = "soit-db-pro-2.ucc.usyd.edu.au"

    # Create a connection to the database
    conn = None
    try:
        # Parses the config file and connects using the connect string
        conn = psycopg2.connect(database=userid,
                                    user=userid,
                                    password=passwd,
                                    host=myHost)

    except psycopg2.Error as sqle:
        print("psycopg2.Error : " + sqle.pgerror)
    
    # return the connection to use
    return conn


cursor = openConnection().cursor()

'''
Validate administrator based on login and password
'''
def checkAdmCredentials(login, password):
    cursor.execute("SELECT * FROM administrator WHERE login = %s AND password = %s", (login, password))
    return cursor.fetchone()



'''
List all the associated instructions in the database by administrator
'''


def findCustomerNameByLogin(customer_login):
    cursor.execute("SELECT firstname, lastname FROM customer WHERE login = %s", (customer_login,))
    return cursor.fetchone()[0] + "/n" + cursor.fetchone()[1]


def findEtfNameByCode(etf_code):
    cursor.execute("SELECT name FROM etf WHERE code = %s", (etf_code,))
    return cursor.fetchone()[0]


def findInstructionsByAdm(login):
    all_instructions = []
    cursor.execute("SELECT * FROM investinstruction WHERE administrator = %s order by expirydate asc, customer desc ", (login,))
    for instrunction in cursor.fetchall():
        instrunction_id = instrunction[0]
        amount = instrunction[1]
        frequency = instrunction[2]
        expirydate = instrunction[3]
        customer_login = instrunction[4]
        customer_name = findCustomerNameByLogin(customer_login)
        etf_code = instrunction[5]
        etf_name = findEtfNameByCode(etf_code)
        notes = instrunction[6]
        instruction_dict = {'instrction_id': instrunction_id, 'amount': amount, 'frequency': frequency, 'expirydate': expirydate, 'customer': customer_name, 'etf': etf_name, 'notes': notes}
        all_instructions.append(instruction_dict)

    if len(all_instructions) == 0:
        return None
    else:
        return all_instructions

'''
Find a list of instructions based on the searchString provided as parameter
See assignment description for search specification
'''
def findInstructionsByCriteria(searchString):

    return


'''
Add a new instruction
'''
def addInstruction(amount, frequency, customer, administrator, etf, notes):

    return


'''
Update an existing instruction
'''
def updateInstruction(instructionid, amount, frequency, expirydate, customer, administrator, etf, notes):

    return
