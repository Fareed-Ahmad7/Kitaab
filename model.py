# create models / functions for notes

from pickle import NONE


class Note:
    # creating custom constructor
    def __init__(self, idx, title, content):     
        self.idx = idx
        self.title= title
        self.content = content
        
    def __repr__(self) -> str:
        return f"({self.idx},{self.title}, {self.content})"

