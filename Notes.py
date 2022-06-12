import os
import sys
from rich import box
from model import Note
from rich.table import Table
from datetime import datetime
from rich.console import Console
from rich.traceback import install
from database import createNote, deleteNote, get_all_notes, updateContent, updateNote

install()  # overwrites traceback with rich's traceback 

console = Console()
date = datetime.today().strftime('%d/%m/%Y')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    console.print(" 1 --> New note", style="orchid2")
    console.print(" 2 --> Edit note", style="pale_violet_red1")
    console.print(" 3 --> Edit content", style="light_coral")
    console.print(" 4 --> Delete note", style="red3")

def App():
    clear()
    # Creating table using Rich
    table = Table(title="Al-Kitaab", title_style="indian_red1", style="indian_red1", box=box.ROUNDED)
    
    table.add_column("🌵", style="orange3")
    table.add_column("Name", style="orchid1", header_style="orange3")
    table.add_column("Content", style="medium_spring_green",header_style="orange3")
    table.add_column("Date", style="yellow1",justify="center", header_style="orange3")
    
    # query all notes from database
    Notes = get_all_notes()
    for idx, task in enumerate(Notes, start=1):
        table.add_row(str(idx), task.name, task.content[:30], task.date_Added)
    console.print(table)
    
    print("\n")
    menu()
    
    response = input(" 🦄 ")
    
    if int(response) == 1:
        idx = 0
        NoteName = input(" Name: ")
        NoteContent = input(" Content: ")
        Date = date
        note = Note(idx, NoteName, NoteContent, Date)
        createNote(note)
        clear()
        App()
    elif int(response) == 2:
        name_input = str(input(" Note name:"))
        etc = '%'
        note_name = name_input+etc
        new_name = str(input(" New name: "))
        updateNote(note_name, new_name)
        clear()
        App()
    elif int(response) == 3:
        name_input = str(input(" Note name:"))
        etc = '%'
        note_name = name_input+etc
        new_content = str(input(" New content: "))
        updateContent(note_name, new_content)
        clear()
        App()
    elif int(response) == 4:
        name_input = str(input(" Note name:"))
        etc = '%'
        note_name = name_input+etc
        deleteNote(note_name)
        clear()
        App()
    else:
        # clear()
        print("\n")
        console.print("oops! invalid input 😓", style="orchid2")
        console.print("type 1 to Create a new note", style="orchid2")
        console.print("type 2 to Edit note", style="orchid2")
        console.print("type 3 to Edit note content", style="orchid2")
        console.print("type 4 to Delete note", style="orchid2")


if __name__ == "__main__":
    try:
        App()
    except KeyboardInterrupt:
        clear()
        sys.exit(0)
