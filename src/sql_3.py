'''
Student roster
--------------
This application will read roster data in JSON format, parse the file, and then produce an SQLite database 
that contains a User, Course, and Member table and populate the tables from the data file.

You can base your solution on this code: http://www.py4e.com/code3/roster/roster.py .
This code is incomplete as you need to modify the program to store the role column in the Member table to complete the assignment.

Each student gets their own file for the assignment. 
Download this file (https://www.py4e.com/tools/sql-intro/roster_data.php?PHPSESSID=6cf994430eba571d8e4deec38a27f5eb)
and save it as roster_data.json. 
Move the downloaded file into the same folder as your roster.py program.

Once you have made the necessary changes to the program and it has been run successfully reading the above JSON data, run the following SQL command:

SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X

Find the first row in the resulting record set and enter the long string that looks like 53656C696E613333.
'''

import sys
import utils
import json

def main(argv):
    (db_connection, db_cursor) = utils.create_db_connection('../data/students.sqlite')
    prepare_db(db_cursor)
    file_handle = utils.open_file_to_handle(argv)
    json_data = json.loads(file_handle.read())
    load_records(json_data, db_connection, db_cursor)
    print(get_hex(db_cursor))
    return

def prepare_db(db_cursor):
    db_cursor.executescript('''
        DROP TABLE IF EXISTS User;
        DROP TABLE IF EXISTS Member;
        DROP TABLE IF EXISTS Course;

        CREATE TABLE User (
            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name   TEXT UNIQUE
        );

        CREATE TABLE Course (
            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            title  TEXT UNIQUE
        );

        CREATE TABLE Member (
            user_id     INTEGER,
            course_id   INTEGER,
            role        INTEGER,
            PRIMARY KEY (user_id, course_id)
        )
    '''
    )

def load_records(json_data, db_connection, db_cursor):
    commit_counter = 0
    for entry in json_data:
        user_name = entry[0]
        course_title = entry[1]
        member_role = entry[2]

        db_cursor.execute('INSERT OR IGNORE INTO User (name) VALUES ( ? )', (user_name,))
        db_cursor.execute('SELECT id FROM User WHERE name = ? ', (user_name,))
        user_id = db_cursor.fetchone()[0]

        db_cursor.execute('INSERT OR IGNORE INTO Course (title) VALUES ( ? )', (course_title,))
        db_cursor.execute('SELECT id FROM Course WHERE title = ? ', (course_title,))
        course_id = db_cursor.fetchone()[0]

        db_cursor.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES ( ?, ?, ? )', (user_id, course_id, member_role))

        commit_counter += 1
        if commit_counter == 10:
            db_connection.commit()
            commit_counter = 0

    db_connection.commit()

    return

def get_hex(db_cursor):
    query = """
        SELECT hex(User.name || Course.title || Member.role ) AS X 
        FROM User JOIN Member JOIN Course 
            ON User.id = Member.user_id AND Member.course_id = Course.id
        ORDER BY X
    """
    result = db_cursor.execute(query)
    result_hex = result.fetchone()
    return result_hex

if __name__ == "__main__":
    main(sys.argv[1:])