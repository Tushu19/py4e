'''
Musical Track Database
This application will read an iTunes export file in XML and produce a properly normalized database with this structure:

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);

If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.py4e.com/code3/tracks.zip. 
The ZIP file contains the Library.xml file to be used for this assignment. 
You can export your own tracks from iTunes and create a database, but for the database that you turn in for this assignment, only use the Library.xml data that is provided.

To grade this assignment, the program will run a query like this on your uploaded database and look for the data it expects to see:

SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3

The expected result of the modified query on your database is: (shown here as a simple HTML table with titles)

Track	Artist	Album	Genre
Chase the Ace	AC/DC	Who Made Who	Rock
D.T.	AC/DC	Who Made Who	Rock
For Those About To Rock (We Salute You)	AC/DC	Who Made Who	Rock
'''

import sys
import utils
import xml.etree.ElementTree as ET

def main(argv):
    (db_connection, db_cursor) = utils.create_db_connection(db_address = '../data/tracks.sqlite')
    prepare_tracks_db(db_cursor)
    input_file_handle = utils.open_file_to_handle(argv)
    xml_root = utils.open_xml(input_file_handle)
    track_list = extract_track_elements(xml_root)
    load_tracks(track_list, db_cursor, db_connection)
    print_results(db_cursor)
    return
    

def prepare_tracks_db(db_cursor):
    db_cursor.execute('DROP TABLE IF EXISTS Artist;')
    db_cursor.execute(
    '''
        CREATE TABLE Artist (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE
        );
    '''
    )

    db_cursor.execute('DROP TABLE IF EXISTS Genre;')
    db_cursor.execute(
        '''
        CREATE TABLE Genre (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE
        );
        '''
    )

    db_cursor.execute('DROP TABLE IF EXISTS Album;')
    db_cursor.execute(
        '''
        CREATE TABLE Album (
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            artist_id  INTEGER,
            title   TEXT UNIQUE
        );
        '''
    )

    db_cursor.execute('DROP TABLE IF EXISTS Track;')
    db_cursor.execute(
        '''
        CREATE TABLE Track (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            title TEXT UNIQUE,
            album_id INTEGER,
            genre_id INTEGER,
            len INTEGER, 
            rating INTEGER, 
            count INTEGER
        );
        '''
    )

    return


def extract_track_elements(xml_root):
    track_data = [dict_elem for dict_elem in xml_root.iter('dict')][0]
    track_list = [track for track in track_data.findall("./dict/dict")]
    return track_list


def load_tracks(track_list, db_cursor, db_connection):

    for track_element in track_list:
        artist_name = ''
        genre_name = ''
        album_title = ''
        track_title = ''
        track_length = 0
        track_rating = 0
        play_count = 0

        track_field_elements = [child_element for child_element in track_element]

        for field_index in range(len(track_field_elements)):
            element = track_field_elements[field_index]

            if element.tag != 'key':
                continue

            if  element.text == 'Artist':
                artist_name = track_element[field_index + 1].text
            elif element.text == 'Genre':
                genre_name = track_element[field_index + 1].text
            elif element.text == 'Album':
                album_title = track_element[field_index + 1].text
            elif element.text == 'Name':
                track_title = track_element[field_index + 1].text
            elif element.text == 'Total Time':
                track_length = int(track_element[field_index + 1].text)
            elif element.text == 'Rating':
                track_rating = int(track_element[field_index + 1].text)
            elif element.text == 'Play Count':
                play_count = int(track_element[field_index + 1].text)

        artist_id = put_artist(artist_name, db_cursor)
        genre_id = put_genre(genre_name, db_cursor)
        album_id = put_album(album_title, artist_id, db_cursor)
        track_id = put_track(track_title, album_id, genre_id, track_length, track_rating, play_count, db_cursor)

        db_connection.commit()

    return


def put_artist(artist_name, db_cursor):
    db_cursor.execute('SELECT name FROM Artist WHERE name = ? ', (artist_name,))
    row = db_cursor.fetchone()

    if row is None:
        db_cursor.execute('INSERT INTO Artist (name) VALUES (?)', (artist_name,))
    
    db_cursor.execute('SELECT id FROM Artist WHERE name = ?', (artist_name,))
    artist_id = db_cursor.fetchone()[0]

    return artist_id


def put_genre(genre_name, db_cursor):
    db_cursor.execute('SELECT name FROM Genre WHERE name = ? ', (genre_name,))
    row = db_cursor.fetchone()

    if row is None:
        db_cursor.execute('''INSERT INTO Genre (name) VALUES (?)''', (genre_name,))

    db_cursor.execute('SELECT id FROM Genre WHERE name = ?', (genre_name,))
    genre_id = db_cursor.fetchone()[0]
    
    return genre_id


def put_album(album_title, artist_id, db_cursor):
    db_cursor.execute('SELECT title FROM Album WHERE title = ? ', (album_title,))
    row = db_cursor.fetchone()

    if row is None:
        db_cursor.execute('''INSERT INTO Album (artist_id, title) VALUES (?, ?)''', (artist_id, album_title))

    db_cursor.execute('SELECT id FROM Album WHERE title = ?', (album_title,))
    album_id = db_cursor.fetchone()[0]
    
    return album_id


def put_track(track_title, album_id, genre_id, track_length, track_rating, play_count, db_cursor):
    db_cursor.execute('SELECT title FROM Track WHERE title = ? ', (track_title,))
    row = db_cursor.fetchone()

    if row is None:
        db_cursor.execute('''
            INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?)
            ''', (track_title, album_id, genre_id, track_length, track_rating, play_count))

    db_cursor.execute('SELECT id FROM Track WHERE title = ?', (track_title,))
    track_id = db_cursor.fetchone()[0]
    
    return track_id


def print_results(db_cursor):
    query = """
    SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
    """

    results = (db_cursor.execute(query))
    for result_row in results.fetchall():
        print(result_row)

    return


if __name__ == "__main__":
    main(sys.argv[1:])