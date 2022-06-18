import sqlite3
from model import Note
from typing import List

# connect to database
conn = sqlite3.connect('notes.db')

# create a cursor
c = conn.cursor()

# create a table
def createTable():
    c.execute(""" CREATE TABLE IF NOT EXISTS notes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title text,
            content text,
            dateAdded text
        )""")

createTable()

def tokenTable():
    c.execute(""" CREATE TABLE IF NOT EXISTS Token(
            token text
        )""")

tokenTable()

def dropToken():
    with conn:
        c.execute(""" DROP TABLE IF EXISTS Token """)
        conn.commit()
    

def addToken(mytoken: str):
    dropToken()
    tokenTable()
    with conn:
        c.execute("INSERT INTO Token(token) VALUES(:token)", {'token': mytoken})
        conn.commit()
        
def showToken():
    tokenTable()
    with conn:
        c.execute("SELECT token from Token")
        tokens = None
        tokens = c.fetchone()
        if tokens!= None:
            for token in tokens:
                return token
        else:
            return tokens               
                
        
def createNote(note: Note):
    with conn:
        c.execute("INSERT INTO notes(title, content, dateAdded) VALUES( :title, :content, :dateAdded)", {'title': note.name, 'content': note.content, 'dateAdded': note.date_Added})
        conn.commit()


# to access specific note content
def getNote(new_name: str):
    with conn:
        c.execute('''SELECT content from notes WHERE title LIKE ?''',(new_name,))
        rows = c.fetchone()
        for row in rows:
            return row


def updateNote(noteName: str, newName: str , newDate: str):
    with conn:
        c.execute('''UPDATE notes SET title = ? WHERE title LIKE ? ''', (newName, noteName,))
        conn.commit()
    with conn:
        c.execute('''UPDATE notes SET dateAdded = ? WHERE title LIKE ? ''', (newDate, newName,))
        conn.commit()


def updateContent(noteName: str, newContent: str, newDate: str):
    with conn:
        c.execute('''UPDATE notes SET content = ? WHERE title LIKE ? ''', (newContent, noteName,))
        conn.commit()
    with conn:
        c.execute(
            '''UPDATE notes SET dateAdded = ? WHERE title LIKE ? ''', (newDate, noteName,))
        conn.commit()
  
  
def deleteNote(noteName: str):
    with conn:
        c.execute('''DELETE FROM notes WHERE title LIKE ? ''', (noteName,))
        conn.commit()
    
    
def get_all_notes() -> List[Note]:
    c.execute("SELECT * from notes")
    results = c.fetchall()
    notes = []
    for result in results:
        notes.append(Note(*result))
    return notes


def get_dict():
    with conn:
        conn.row_factory = sqlite3.Row
        curs = conn.cursor()
        curs.execute("SELECT * FROM notes")
        rows = curs.fetchall()
        Dict =[]
        for row in rows:
            Dict.append(dict(row))
        return Dict  
