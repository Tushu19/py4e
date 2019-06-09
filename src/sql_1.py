'''
Counting Organizations
This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) 
using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)

When you have run the program on mbox.txt upload the resulting database file above for grading.
If you run the program multiple times in testing or with dfferent files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.
The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.

Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in the loop, 
it might take as long as a few minutes to process all the data. 
The commit insists on completely writing all the data to disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside of the loop. 
In any database program, there is a balance between the number of operations you execute between commits 
and the importance of not losing the results of operations that have not yet been committed.
'''

import sqlite3

def main():
    (connection, cursor) = create_db_connection()
    prepare_database(cursor)
    file_path = prompt_file_path()
    file_handle = open_file(file_path)
    write_domains_to_database(file_handle, connection, cursor)
    get_results(cursor)
    cursor.close()
    return

def create_db_connection():
    connection = sqlite3.connect('../data/emaildb.sqlite')
    cursor = connection.cursor()
    return (connection, cursor)

def prepare_database(cur):
    cur.execute('DROP TABLE IF EXISTS Counts')
    cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

def prompt_file_path():
    file_path = input('Enter input file path: ')
    if (len(file_path) < 1): file_path = '../data/mbox-short.txt'
    return file_path

def open_file(file_path):
    try:
        file_handle = open(file_path)
    except:
        print('No such file found.')
        exit
    
    return file_handle

def write_domains_to_database(file_handle, db_connection, db_cursor):
    # Read file line by line and
        # Filter 'From:' lines
        # Extract sender's organization
        # Write or update to SQL DB
        # (On every 10th iteration) Commit commands to database

    iter_count = 0
    commit_interval = 50

    for line in file_handle:
        if not line.startswith('From: '): continue
        pieces = line.split()
        email_address = pieces[1]
        email_components = email_address.split('@')
        email_domain = email_components[1]
        db_cursor.execute('SELECT count FROM Counts WHERE org = ? ', (email_domain,))
        row = db_cursor.fetchone()
        
        if row is None:
            db_cursor.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, 1)''', (email_domain,))
        else:
            db_cursor.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                        (email_domain,))
        
        if iter_count % commit_interval == 0: 
            db_connection.commit()
    
    db_connection.commit()
    
    return

def get_results(db_cursor):
    # https://www.sqlite.org/lang_select.html
    sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

    for row in db_cursor.execute(sqlstr):
        print(str(row[0]), row[1])

    return

if __name__ == "__main__":
    main()