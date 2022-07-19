'''
    This module has ready to use sqlite query functions.
'''

import sqlite3
from typing import List
from model import Note

# connect to database
conn = sqlite3.connect('notes.db')

# create a cursor
c = conn.cursor()


def create_table():
    '''
        create notes table in database.
    '''

    c.execute(""" CREATE TABLE IF NOT EXISTS notes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title text,
            content text,
            dateAdded text
        )""")


create_table()


def token_table():
    '''
        create token table in database.
    '''

    c.execute(""" CREATE TABLE IF NOT EXISTS Token(
            token text
        )""")


token_table()


def drop_token():
    '''
        delete token from the table.
    '''

    with conn:
        c.execute(""" DROP TABLE IF EXISTS Token """)
        conn.commit()


def add_token(mytoken: str):
    '''
        adds token to table.
    '''

    drop_token()
    token_table()
    with conn:
        c.execute("INSERT INTO Token(token) VALUES(:token)",
                  {'token': mytoken})
        conn.commit()


def show_token():
    '''
        fetch token from the table.
    '''

    token_table()
    with conn:
        c.execute("SELECT token from Token")
        tokens = None
        tokens = c.fetchone()
        if tokens is not None:
            for token in tokens:
                return token
        else:
            return tokens


def create_note(note: Note):
    '''
        add new note.
    '''

    with conn:
        c.execute("INSERT INTO notes(title, content, dateAdded) VALUES( :title, :content, :dateAdded)",
                  {'title': note.name, 'content': note.content, 'dateAdded': note.date_Added})
        conn.commit()


def get_note(new_name: str):
    '''
        access content from specific note.
    '''

    with conn:
        c.execute('''SELECT content from notes WHERE title LIKE ?''', (new_name,))
        rows = c.fetchone()
        for row in rows:
            return row


def update_note_name(noteName: str, newName: str, newDate: str):
    '''
        edit note name.
    '''

    with conn:
        c.execute('''UPDATE notes SET title = ? WHERE title LIKE ? ''',
                  (newName, noteName,))
        conn.commit()
    with conn:
        c.execute(
            '''UPDATE notes SET dateAdded = ? WHERE title LIKE ? ''', (newDate, newName,))
        conn.commit()


def update_note_content(noteName: str, newContent: str, newDate: str):
    '''
        edit note content.
    '''

    with conn:
        c.execute('''UPDATE notes SET content = ? WHERE title LIKE ? ''',
                  (newContent, noteName,))
        conn.commit()
    with conn:
        c.execute(
            '''UPDATE notes SET dateAdded = ? WHERE title LIKE ? ''', (newDate, noteName,))
        conn.commit()


def delete_note(noteName: str):
    '''
        delete note.
    '''

    with conn:
        c.execute('''DELETE FROM notes WHERE title LIKE ? ''', (noteName,))
        conn.commit()


def get_all_notes() -> List[Note]:
    '''
        fetch all notes from the table.
    '''

    c.execute("SELECT * from notes")
    results = c.fetchall()
    notes = []
    for result in results:
        notes.append(Note(*result))
    return notes


def get_dict():
    '''
    fetch all notes & add to dictionary.
    '''

    with conn:
        conn.row_factory = sqlite3.Row
        curs = conn.cursor()
        curs.execute("SELECT * FROM notes")
        rows = curs.fetchall()
        Dict = []
        for row in rows:
            Dict.append(dict(row))
        return Dict
