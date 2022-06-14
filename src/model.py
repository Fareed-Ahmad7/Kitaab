class Note:
    def __init__(self, idx, name, content, date_Added):
        self.idx = idx
        self.name = name
        self.content = content
        self.date_Added = date_Added
        
    def __repr__(self) -> str:
        return f"({self.idx},{self.name}, {self.content}, {self.date_Added})"
