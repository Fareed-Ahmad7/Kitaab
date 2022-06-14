import sqlite3
from typing import List
from model import Note

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

def createNote(note: Note):
    with conn:
        c.execute("INSERT INTO notes(title, content, dateAdded) VALUES( :title, :content, :dateAdded)", {'title': note.name, 'content': note.content, 'dateAdded': note.date_Added})
        conn.commit()

def showNote():
        c.execute("SELECT  * from notes")
        rows = c.fetchall()  
        for row in rows:
            print(row)        

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
  
