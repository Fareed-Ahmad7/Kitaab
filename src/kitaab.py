import os
import sys
from datetime import datetime
from rich.console import Console
from database import create_note, delete_note, update_note_content, update_note_name, add_token, drop_token
from pygithub import create_github_note, edit_github_note_name, edit_github_note_content, delete_github_note, check_token_validity
from terminal import clear, error, menu, Help, print_board, print_table
from model import Note

console = Console()


def loop():

    response = input("🦄 ")

    try:
        # Help
        if response == 'help':
            Help()
            loop()

        # Quit
        elif response in ('quit', 'q'):
            console.print("exited successfully!", style="orchid1")
            os._exit(0)

        # Board
        elif response == 'board':
            print_board()
            loop()

        # Add Token
        elif response == 'add-token':
            console.print("Adding token requires restart!", style="yellow3")
            token = input("Enter github personal access token: ")
            add_token(token)
            token_valid = check_token_validity()
            if token_valid is False:
                drop_token()
                console.print(
                    "[red]Invalid token[/] -- please check your token or add a new one", style="light_coral")

        # Create Note
        elif int(response) == 1:
            idx = 0
            note_name = input("Name: ")
            note_content = input("Content: ")
            date = datetime.today().strftime('%d/%b/%H:%M')
            note = Note(idx, note_name, note_content, date)
            create_note(note)
            create_github_note(note_name, note_content)
            clear()
            app()

        # Update Note Name
        elif int(response) == 2:
            note_name = str(input("Note name: "))
            new_name = str(input("New name: "))
            date = datetime.today().strftime('%d/%b/%H:%M')
            update_note_name(note_name, new_name, date)
            edit_github_note_name(note_name, new_name)
            clear()
            app()

        # Update Note Content
        elif int(response) == 3:
            note_name = str(input("Note name: "))
            new_content = str(input("New content: "))
            date = datetime.today().strftime('%d/%b/%H:%M')
            update_note_content(note_name, new_content, date)
            edit_github_note_content(note_name, new_content)
            clear()
            app()

        # Delete Note
        elif int(response) == 4:
            note_name = str(input("Note name: "))
            delete_note(note_name)
            delete_github_note(note_name)
            clear()
            app()

        else:
            error()
            loop()
    except:
        console.print("oops! invalid text input 😓", style="orchid2")
        console.print(
            "use [orchid2]help[/] to list all existing input", style="indian_red1")
        loop()


def app():
    clear()
    print_table()
    menu()
    loop()


if __name__ == "__main__":
    try:
        app()
    except KeyboardInterrupt:
        clear()
        sys.exit(0)
