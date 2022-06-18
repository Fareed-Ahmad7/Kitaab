import os
from github import Github
from database import getNote, showToken, get_all_notes
from rich.console import Console

console = Console()


# Token
key = showToken()
token = os.getenv('GITHUB_TOKEN', key)
g = Github(token)
user = g.get_user()

# checking if token entered by user is valid or not
def checkTokenValidity():
    token_valid = "false" 
    key = showToken()
    token = os.getenv('GITHUB_TOKEN', key)
    g = Github(token)
    user = g.get_user()
    try:
        if key!=None:
            console.print(f"your github account is [yellow3]{user.login}[/]", style="red")
            token_valid = "true"
            return token_valid
    except:
        return token_valid


# checking if kitaab repository exists 
def checkRepoExist():
    exist = "false"
    try:
        repo = user.get_repo("My-Kitaab")
        exist = "true"
        return exist
    except:
        return exist

repoExist = checkRepoExist()


# create note
def createGithubNote(noteName: str, noteContent: str):
    if key != None:
        repo = user.get_repo("My-Kitaab")
        repo.create_file(noteName, "added new note", noteContent)


# create repo
def createGithubRepo():
    if key != None and repoExist == 'false':
        print("please wait...")
        repo = user.create_repo("My-Kitaab")
        repo.create_file("readme.md", "add readme","## This repository is auto created by a note-taking app named kitaab.<br/>learn more https://github.com/Fareed-Ahmad7/Kitaab")
        notes = get_all_notes()
        for note in notes:
            createGithubNote(note.name, note.content)

createGithubRepo()


# edit note name
def editGithubNoteName(noteName: str, newName: str):
    if key != None:
        repo = user.get_repo("My-Kitaab")
        file = repo.get_contents(noteName)
        repo.delete_file(file.path, "deleted note", file.sha)
        noteContent = getNote(newName)
        createGithubNote(newName, noteContent)


# edit note content
def editGithubNoteContent(noteName, newContent):
    if key != None:
        repo = user.get_repo("My-Kitaab")
        file = repo.get_contents(noteName)
        repo.update_file(file.path, "edited note content", newContent, file.sha)


# delete note
def deleteGithubNote(noteName: str):
    if key != None:
        repo = user.get_repo("My-Kitaab")
        file = repo.get_contents(noteName)
        repo.delete_file(file.path, "deleted note", file.sha)
