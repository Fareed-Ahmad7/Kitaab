import os
import sys
from model import Note
from rich.table import Table
from datetime import datetime
from rich.console import Console
from database import createNote, deleteNote, get_all_notes, updateContent, updateNote

date = datetime.today().strftime('%d/%m/%Y')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
        

def menu():
    clear()
    # Creating table using Rich
    table = Table(title="Al-Kitaab", style="red")

    table.add_column("🌵", style="cyan")
    table.add_column("Name", style="violet")
    table.add_column("Content", style="green")
    table.add_column("Date", style="yellow", justify="center")
    
    # query all notes from database
    Notes = get_all_notes()
    for idx, task in enumerate(Notes, start=1):
        table.add_row(str(idx), task.name, task.content[:30], date)
    console = Console()
    console.print(table)
    
    # Menu

    print("1 --> New note")
    print("2 --> Edit note")
    print("3 --> Edit content")
    print("4 --> Delete note")

    response = int(input("> "))

    if response == 1:
        idx = 0
        NoteName = input("Name: ")
        NoteContent = input("Content: ")
        note = Note(idx, NoteName, NoteContent)
        createNote(note)
        clear()
        menu()
    elif response == 2:
        name_input = str(input("Note name:"))
        etc = '%'
        note_name = name_input+etc
        new_name = str(input("New name: "))
        updateNote(note_name, new_name)
        clear()
        menu()
    elif response == 3:
        name_input = str(input("Note name:"))
        etc = '%'
        note_name = name_input+etc
        new_content = str(input("New content: "))
        updateContent(note_name, new_content)
        clear()
        menu()
    elif response == 4:
        name_input = str(input("Note name:"))
        etc = '%'
        note_name = name_input+etc
        deleteNote(note_name)
        clear()
        menu()
    elif response == 4:
        pass
    else:
        clear()
        sys.exit(0)


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        clear()
        sys.exit(0)
