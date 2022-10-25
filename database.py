#!/usr/bin/env python3
import psycopg2
from datetime import datetime
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


# def findCustomerNameByLogin(customer_login):
#     cursor.execute("SELECT firstname, lastname FROM customer WHERE login = %s", (customer_login,))
#     customer_name = cursor.fetchone()
#     return customer_name[0] + '/n' + customer_name[1]


# def findEtfNameByCode(etf_code):
#     cursor.execute("SELECT name FROM etf WHERE code = %s", (etf_code,))
#     return cursor.fetchone()[0]
#
#
# def getFrequencyDesc(frequency_code):
#     cursor.execute("SELECT frequencydesc FROM frequency WHERE frequencycode = %s", (frequency_code,))
#     return cursor.fetchone()[0]


def findInstructionsByAdm(login):
    all_instructions = []
    # cursor.execute("SELECT * FROM investinstruction WHERE administrator = %s order by expirydate asc, customer desc ", (login,))
    cursor.execute('''SELECT i.InstructionId AS ID, i.Amount AS amount, f.frequencydesc AS frequency, i.ExpiryDate AS Expiry, CONCAT(c.FirstName, ' ', c.LastName) AS Customer, e.Name AS ETF, i.Notes
                        FROM InvestInstruction i
                        JOIN Customer c ON (Customer=Login)
                        JOIN ETF e USING (Code)
                        JOIN Frequency f ON(i.frequency = f.frequencycode) 
                        WHERE Administrator = %s AND ExpiryDate >= CURRENT_DATE
                        ORDER BY ExpiryDate, Customer DESC''', (login,))
    
    for instruction in cursor.fetchall():
        instruction_id = instruction[0]
        amount = instruction[1]
        frequency = instruction[2]
        expirydate = instruction[3]
        expirydate = expirydate.strftime("%d-%m-%Y")
        customer = instruction[4]
        etf = instruction[5]
        if instruction[6] == None:
            notes = ''
        else:
            notes = instruction[6]
        instruction_dict_valid = {'instruction_id': instruction_id, 'amount': amount, 'frequency': frequency, 'expirydate': expirydate, 'customer': customer, 'etf': etf, 'notes': notes}
        all_instructions.append(instruction_dict_valid)

    cursor.execute('''SELECT i.InstructionId AS ID, i.Amount AS amount, f.frequencydesc AS frequency, i.ExpiryDate AS Expiry, CONCAT(c.FirstName, ' ', c.LastName) AS Customer, e.Name AS ETF, i.Notes
                    FROM InvestInstruction i
                    JOIN Customer c ON (Customer=Login)
                    JOIN ETF e USING (Code)
                    JOIN Frequency f ON(i.frequency = f.frequencycode) 
                    WHERE Administrator = %s AND ExpiryDate < CURRENT_DATE
                    ORDER BY ExpiryDate, Customer DESC''', (login,))
        
    for instruction in cursor.fetchall():
        instruction_id = instruction[0]
        amount = instruction[1]
        frequency = instruction[2]
        expirydate = instruction[3]
        expirydate = expirydate.strftime("%d-%m-%Y")
        customer = instruction[4]
        etf = instruction[5]
        if instruction[6] == None:
            notes = ''
        else:
            notes = instruction[6]
        instruction_dict_invalid = {'instruction_id': instruction_id, 'amount': amount, 'frequency': frequency, 'expirydate': expirydate, 'customer': customer, 'etf': etf, 'notes': notes}
        all_instructions.append(instruction_dict_invalid)



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
