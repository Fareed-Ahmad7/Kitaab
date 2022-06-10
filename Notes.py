import os
import sys
from model import Note
from rich.table import Table
from datetime import datetime
from rich.console import Console
from database import createNote, deleteNote, get_all_notes

date = datetime.today().strftime('%d/%m/%Y')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
        

def menu():
    clear()
    # Creating table using Rich
    table = Table(title="Al-Kitaab", style="red")

    table.add_column("🌵", style="cyan")
    table.add_column("Note", style="violet")
    table.add_column("Content", style="green")
    table.add_column("Date Added", style="yellow", justify="center")
    
    # query all notes from database
    Notes = get_all_notes()
    for idx, task in enumerate(Notes, start=1):
        table.add_row(str(idx), task.title, task.content[:30], date)
    console = Console()
    console.print(table)
    
    # Menu

    print("1 --> New note")
    print("2 --> Delete note")

    response = int(input("> "))

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
