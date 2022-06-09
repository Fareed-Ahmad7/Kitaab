import os
import sys
from model import Note
from rich.table import Table
from rich.console import Console
from database import createNote, deleteNote, get_all_notes


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
        

def menu():
    # global idx
    clear()
    # Creating table using Rich
    table = Table(title="Al-Kitaab")

    table.add_column("#")
    table.add_column("Note")
    table.add_column("content")
    table.add_column("Date Added")
    
    # query all notes from database
    Notes = get_all_notes()
    for idx, task in enumerate(Notes, start=1):
        table.add_row(str(idx), task.title, task.content,"Today" )
    console = Console()
    console.print(table)
    
    # Menu
    print("\n")
    print("1 --> New note")
    print("2 --> Delete note")

    response = int(input(">"))

    if response == 1:
        idx = 0
        NoteTitle = input("Title: ")
        NoteContent = input("Note: ")
        note = Note(idx, NoteTitle, NoteContent)
        createNote(note)
        clear()
        menu()
    elif response == 2:
        rowid = int(input("delete:"))
        deleteNote(rowid)
        # updateNote()
        clear()
        menu()
    else:
        clear()
        sys.exit(0)


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        clear()
        sys.exit(0)
