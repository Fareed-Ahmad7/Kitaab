'''
    This module has functions that are responsible for publishing notes to Github.
'''

import os
from github import Github
from rich.console import Console
from database import get_note, show_token, get_all_notes

console = Console()


# Token
key = show_token()
token = os.getenv('GITHUB_TOKEN', key)
g = Github(token)
user = g.get_user()


def check_token_validity():
    '''
        checking if token entered by user is valid or not.
    '''

    token_valid = False
    key = show_token()
    token = os.getenv('GITHUB_TOKEN', key)
    g = Github(token)
    user = g.get_user()
    try:
        if key is not None:
            console.print(
                f"your github account is [yellow3]{user.login}[/]", style="red")
            token_valid = True
            return token_valid
    except:
        return token_valid


def check_repo_exist():
    '''
        checking if kitaab repository exists.
    '''

    exist = False
    try:
        user.get_repo("My-Kitaab")
        exist = True
        return exist
    except:
        return exist


REPO_EXIST = check_repo_exist()


def create_github_note(noteName: str, noteContent: str):
    '''
        commit note to repository.
    '''

    if key is not None:
        repo = user.get_repo("My-Kitaab")
        repo.create_file(noteName, "added new note", noteContent)


def create_github_repo():
    '''
        create My-Kitaab repository.
    '''

    if key is not None and REPO_EXIST is False:
        print("please wait...")
        repo = user.create_repo("My-Kitaab")
        repo.create_file("readme.md", "add readme",
                         "## This repository is auto created by a note-taking app named kitaab.<br/>learn more https://github.com/Fareed-Ahmad7/Kitaab")
        notes = get_all_notes()
        for note in notes:
            create_github_note(note.name, note.content)


create_github_repo()


def edit_github_note_name(noteName: str, newName: str):
    '''
        commit new note name.
    '''

    if key is not None:
        repo = user.get_repo("My-Kitaab")
        file = repo.get_contents(noteName)
        repo.delete_file(file.path, "deleted note", file.sha)
        note_content = get_note(newName)
        create_github_note(newName, note_content)


def edit_github_note_content(noteName: str, newContent: str):
    '''
        commit new note content.
    '''

    if key is not None:
        repo = user.get_repo("My-Kitaab")
        file = repo.get_contents(noteName)
        repo.update_file(file.path, "edited note content",
                         newContent, file.sha)


def delete_github_note(noteName: str):
    '''
        delete note from the repository.
    '''

    if key is not None:
        repo = user.get_repo("My-Kitaab")
        file = repo.get_contents(noteName)
        repo.delete_file(file.path, "deleted note", file.sha)
