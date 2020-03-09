"""Opens and readers the entire file"""
__name__ = "filereader"
class MyReader:
    def __init__(self, flpath):
        self.flp_path = flpath

    flp_path = ""

    def ReadFileData(self):
        f= open(self.flp_path, "r")
        print(f.read())


