'''
    This module has functions that print content on terminal.
'''

import os
from rich.console import Console
from rich.columns import Columns
from rich import box, print
from rich.panel import Panel
from rich.table import Table
from database import get_dict, get_all_notes

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
    print("\n")
    console.print(" 1 --> New note", style="orchid2")
    console.print(" 2 --> Edit name", style="pale_violet_red1")
    console.print(" 3 --> Edit content", style="light_coral")
    console.print(" 4 --> Delete note", style="red3")


def Help():
    console.print(
        " type add-token --> setup github integration ", style="red3")
    console.print(" type board --> view notes as board ", style="light_coral")
    console.print(" type quit or q -->  to exit ", style="pale_violet_red1")


def print_table():
    '''
        Creating table using Rich.
    '''

    table = Table(title="Al-kitaab", title_style="indian_red1",
                  style="indian_red1", box=box.ROUNDED)

    table.add_column("🌵", style="orange3")
    table.add_column("Name", style="orchid1", header_style="orange3")
    table.add_column("Content", style="medium_spring_green",
                     header_style="orange3")
    table.add_column("Last Modified", style="yellow1",
                     justify="center", header_style="orange3")

    # get all notes from database
    notes = get_all_notes()
    for idx, note in enumerate(notes, start=1):
        table.add_row(str(idx), note.name, note.content[:30], note.date_Added)
    console.print(table)


# BOARD VIEW
def get_content(user):
    '''
        getting content for board view.
    '''

    content = user["content"]
    name = user["title"]
    return f"[medium_spring_green]{content}\n[orchid1]{name}"


def print_board():
    '''
        building board view with Rich.
    '''

    console = Console()
    users = get_dict()
    if users == []:
        console.print("notebook is empty", style='yellow3')
    else:
        user_renderables = [Panel(get_content(
            user), expand=True,  border_style="indian_red1")for user in users]
        console.print(Columns(user_renderables))
