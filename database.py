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
            content text
        )""")

createTable()

def createNote(note: Note):
    with conn:
        c.execute("INSERT INTO notes(title, content) VALUES( :title, :content)",{ 'title': note.title, 'content': note.content})
        conn.commit()
    
def showNote():
        c.execute("SELECT  * from notes")
        rows = c.fetchall()  
        for row in rows:
            print(row)        
showNote()


def get_all_notes() -> List[Note]:
    c.execute("SELECT * from notes")
    results = c.fetchall()
    notes = []
    for result in results:
        notes.append(Note(*result))
    return notes


def deleteNote(delete_rowid: int):
    c.execute('''DELETE FROM notes WHERE rowid = ? ''', (delete_rowid,))
    conn.commit()

# def updateNote():
#     # c.execute(''' UPDATE notes SET rowid=rowid-3 ''')
#     # c.execute('''DELETE from notes''')
#         # c.execute('''DELETE from SQLITE_SEQUENCE WHERE NAME = 'notes' ''')
#         print("ds")
#         c.execute('''UPDATE SQLITE_SEQUENCE SET SEQ = 1 WHERE NAME = "notes" ''')
#         conn.commit()


    
