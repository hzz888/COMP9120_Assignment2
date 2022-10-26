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
    userid = "y22s2c9120_lwan6402"
    passwd = "Qweasdzxc"
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


'''
Validate administrator based on login and password
'''


def checkAdmCredentials(login, password):
    connection = openConnection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM administrator WHERE login = %s AND password = %s", (login, password))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result


'''
List all the associated instructions in the database by administrator
'''


# noinspection DuplicatedCode
def findInstructionsByAdm(login):
    connection = openConnection()
    cursor = connection.cursor()

    all_instructions = []

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
        if instruction[6] is None:
            notes = ''
        else:
            notes = instruction[6]
        instruction_dict_valid = {'instruction_id': instruction_id, 'amount': amount, 'frequency': frequency,
                                  'expirydate': expirydate, 'customer': customer, 'etf': etf, 'notes': notes}
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
        if instruction[6] is None:
            notes = ''
        else:
            notes = instruction[6]
        instruction_dict_invalid = {'instruction_id': instruction_id, 'amount': amount, 'frequency': frequency,
                                    'expirydate': expirydate, 'customer': customer, 'etf': etf, 'notes': notes}
        all_instructions.append(instruction_dict_invalid)

    cursor.close()
    connection.close()

    if len(all_instructions) == 0:
        return None
    else:
        return all_instructions


'''
Find a list of instructions based on the searchString provided as parameter
See assignment description for search specification
'''


def findInstructionsByCriteria(searchString):
    connection = openConnection()
    cursor = connection.cursor()

    found_instructions = []

    cursor.execute('''SELECT i.InstructionId AS ID, i.Amount AS amount, f.frequencydesc AS frequency, i.ExpiryDate AS Expiry, CONCAT(c.FirstName, ' ', c.LastName) AS Customer, e.Name AS ETF, i.Notes
                    FROM InvestInstruction i
                    JOIN Customer c ON (Customer=Login)
                    JOIN ETF e USING (Code)
                    JOIN Frequency f ON(i.frequency = f.frequencycode) 
                    WHERE (CONCAT(c.FirstName, ' ', c.LastName) ILIKE '%%' || %s || '%%' OR e.name ILIKE '%%' || %s || '%%' OR i.notes ILIKE '%%' || %s || '%%') AND i.ExpiryDate >= CURRENT_DATE AND i.Administrator IS NULL
                    ORDER BY ExpiryDate''', (searchString, searchString, searchString))

    for instruction in cursor.fetchall():
        instruction_id = instruction[0]
        amount = instruction[1]
        frequency = instruction[2]
        expirydate = instruction[3]
        expirydate = expirydate.strftime("%d-%m-%Y")
        customer = instruction[4]
        etf = instruction[5]
        if instruction[6] is None:
            notes = ''
        else:
            notes = instruction[6]
        instruction_dict = {'instruction_id': instruction_id, 'amount': amount, 'frequency': frequency,
                            'expirydate': expirydate, 'customer': customer, 'etf': etf, 'notes': notes}
        found_instructions.append(instruction_dict)

    cursor.execute('''SELECT i.InstructionId AS ID, i.Amount AS amount, f.frequencydesc AS frequency, i.ExpiryDate AS Expiry, CONCAT(c.FirstName, ' ', c.LastName) AS Customer, e.Name AS ETF, i.Notes
                    FROM InvestInstruction i
                    JOIN Customer c ON (Customer=Login)
                    JOIN ETF e USING (Code)
                    JOIN Frequency f ON(i.frequency = f.frequencycode) 
                    WHERE (CONCAT(c.FirstName, ' ', c.LastName) ILIKE '%%' || %s || '%%' OR e.name ILIKE '%%' || %s || '%%' OR i.Notes ILIKE '%%' || %s || '%%') AND i.ExpiryDate >= CURRENT_DATE AND i.Administrator IS NOT NULL
                    ORDER BY ExpiryDate''', (searchString, searchString, searchString))

    for instruction in cursor.fetchall():
        instruction_id = instruction[0]
        amount = instruction[1]
        frequency = instruction[2]
        expirydate = instruction[3]
        expirydate = expirydate.strftime("%d-%m-%Y")
        customer = instruction[4]
        etf = instruction[5]
        if instruction[6] is None:
            notes = ''
        else:
            notes = instruction[6]
        instruction_dict = {'instruction_id': instruction_id, 'amount': amount, 'frequency': frequency,
                            'expirydate': expirydate, 'customer': customer, 'etf': etf, 'notes': notes}
        found_instructions.append(instruction_dict)

    cursor.close()
    connection.close()

    return found_instructions


def addInstruction(amount, frequency, customer, administrator, etf, notes):
    connection = openConnection()
    cursor = connection.cursor()
    try:
        cursor.callproc('addInstruction', [amount, frequency, customer, administrator, etf, notes])
        connection.commit()
        cursor.close()
        connection.close()
        return True

    except psycopg2.Error as sqle:
        connection.rollback()
        cursor.close()
        connection.close()
        print(sqle)
        return False


def updateInstruction(instructionid, amount, frequency, expirydate, customer, administrator, etf, notes):
    connection = openConnection()
    cursor = connection.cursor()
    try:
        cursor.callproc('updateInstruction',
                        [instructionid, amount, frequency, expirydate, customer, administrator, etf, notes])
        connection.commit()
        cursor.close()
        connection.close()
        return True

    except psycopg2.Error as sqle:
        connection.rollback()
        cursor.close()
        connection.close()
        print(sqle)
        return False
