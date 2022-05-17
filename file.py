class File():
    def __init__(self, path):
        self.path=path

    def read(self):
        f = open(self.path, "r")
        self.content = f.read()
        
    def getContents(self):
        return self.content