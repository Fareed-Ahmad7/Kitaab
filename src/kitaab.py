import os
import sys
from rich import box
from rich import print
from model import Note
from rich.panel import Panel
from rich.table import Table
from database import get_dict
from datetime import datetime
from rich.columns import Columns
from rich.console import Console
from database import createNote, deleteNote, get_all_notes, updateContent, updateNote


console = Console()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def error():
    console.print("oops! invalid input 😓", style="orchid2")
    console.print("type 1 to Create a new note", style="orchid2")
    console.print("type 2 to Edit note", style="orchid2")
    console.print("type 3 to Edit note content", style="orchid2")
    console.print("type 4 to Delete note", style="orchid2")  

def menu():
    console.print(" 1 --> New note", style="orchid2")
    console.print(" 2 --> Edit note", style="pale_violet_red1")
    console.print(" 3 --> Edit content", style="light_coral")
    console.print(" 4 --> Delete note", style="red3")

def Help():
    console.print(" type github --> setup github integration ", style="red3")
    console.print(" type board --> view notes as board ", style="light_coral")
    console.print(" type quit or q -->  to exit ", style="pale_violet_red1")

def get_content(user):
    content = user["content"]
    title = user["title"]
    return f"[b]{content}[/b]\n[yellow]{title}"

def viewBoard():
    console = Console()
    users = get_dict()
    user_renderables = [Panel(get_content(user), expand=True) for user in users]
    console.print(Columns(user_renderables))
    
def loop():
    response = input("🦄 ")
    try:
        if response == 'help':
            Help()
            loop()
        elif response == 'quit' or response == 'q':
            console.print("exited successfully!", style="orchid1")
            os._exit(0)
        elif response == 'board':
            viewBoard()
            loop()
        elif int(response) == 1:
            idx = 0
            note_name = input("Name: ")
            note_content = input("Content: ")
            date = datetime.today().strftime('%d/%b/%H:%M')
            note = Note(idx, note_name, note_content, date)
            createNote(note)
            clear()
            app()
        elif int(response) == 2:
            name_input = str(input("Note name: "))
            etc = '%'
            note_name = name_input+etc
            new_name = str(input("New name: "))
            date = datetime.today().strftime('%d/%b/%H:%M')
            updateNote(note_name, new_name, date)
            clear()
            app()
        elif int(response) == 3:
            name_input = str(input("Note name: "))
            etc = '%'
            note_name = name_input+etc
            new_content = str(input("New content: "))
            date = datetime.today().strftime('%d/%b/%H:%M')
            updateContent(note_name, new_content, date)
            clear()
            app()
        elif int(response) == 4:
            name_input = str(input("Note name: "))
            etc = '%'
            note_name = name_input+etc
            deleteNote(note_name)
            clear()
            app()
        else:
            error()
            loop()
    except:
        Help()
        loop()
        
def app():
    clear()
    # Creating table using Rich
    table = Table(title="Al-kitaab", title_style="indian_red1", style="indian_red1", box=box.ROUNDED)
    
    table.add_column("🌵", style="orange3")
    table.add_column("Name", style="orchid1", header_style="orange3")
    table.add_column("Content", style="medium_spring_green", header_style="orange3")
    table.add_column("Last Modified", style="yellow1", justify="center", header_style="orange3")
    
    # query all notes from database
    notes = get_all_notes()
    for idx, task in enumerate(notes, start=1):
        table.add_row(str(idx), task.name, task.content[:30], task.date_Added)
    console.print(table)
    
    print("\n")
    menu()
    loop()
    

if __name__ == "__main__":
    try:
        app()
    except KeyboardInterrupt:
        clear()
        sys.exit(0)
