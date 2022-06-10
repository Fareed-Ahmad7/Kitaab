class Note:
    def __init__(self, idx, name, content):     
        self.idx = idx
        self.name= name
        self.content = content
        
    def __repr__(self) -> str:
        return f"({self.idx},{self.name}, {self.content})"

