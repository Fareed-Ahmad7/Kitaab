import os
import sys
from model import Note
from datetime import datetime
from rich.console import Console
from database import createNote, deleteNote, updateContent, updateNote, addToken, dropToken
from gitApi import createGithubNote, editGithubNoteName, editGithubNoteContent, deleteGithubNote, checkTokenValidity
from terminal import clear, error, menu, Help, printBoard, printTable

console = Console()


def loop():

    response = input("🦄 ")

    try:
        # Help
        if response == 'help':
            Help()
            loop()

        # Quit
        elif response == 'quit' or response == 'q':
            console.print("exited successfully!", style="orchid1")
            os._exit(0)

        # Board
        elif response == 'board':
            printBoard()
            loop()

        # Add Token
        elif response == 'add-token':
            console.print("Adding token requires restart!", style="yellow3")
            token = input("Enter github personal access token: ")
            addToken(token)
            tokenValid = checkTokenValidity()
            if tokenValid == False:
                dropToken()
                console.print("[red]Invalid token[/] -- please check your token or add a new one", style="light_coral")

        # Create Note
        elif int(response) == 1:
            idx = 0
            note_name = input("Name: ")
            note_content = input("Content: ")
            date = datetime.today().strftime('%d/%b/%H:%M')
            note = Note(idx, note_name, note_content, date)
            createNote(note)
            createGithubNote(note_name, note_content)
            clear()
            app()

        # Update Note Name
        elif int(response) == 2:
            note_name = str(input("Note name: "))
            new_name = str(input("New name: "))
            date = datetime.today().strftime('%d/%b/%H:%M')
            updateNote(note_name, new_name, date)
            editGithubNoteName(note_name, new_name)
            clear()
            app()

        # Update Note Content
        elif int(response) == 3:
            note_name = str(input("Note name: "))
            new_content = str(input("New content: "))
            date = datetime.today().strftime('%d/%b/%H:%M')
            updateContent(note_name, new_content, date)
            editGithubNoteContent(note_name, new_content)
            clear()
            app()

        # Delete Note
        elif int(response) == 4:
            note_name = str(input("Note name: "))
            deleteNote(note_name)
            deleteGithubNote(note_name)
            clear()
            app()

        else:
            error()
            loop()
    except:
        console.print("oops! invalid text input 😓", style="orchid2")
        console.print("use [orchid2]help[/] to list all existing input", style="indian_red1")
        loop()


def app():
    clear()
    printTable()
    menu()
    loop()


if __name__ == "__main__":
    try:
        app()
    except KeyboardInterrupt:
        clear()
        sys.exit(0)
