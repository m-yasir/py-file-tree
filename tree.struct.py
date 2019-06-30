class Tree:
    root = None
    string = ""
    def __init__(self):
        self.root = FolderNode("LocalDisk")
        self.string = ""
        return

    def getFolder(self, folderName):
        
        return
    
    def printFolders(self):
        self._populateString(self.root)
        print(self.string)
        self.string = ""
        return
    # a private method used to fill string with all the folder names
    def _populateString(self, myRoot):
        if not myRoot or myRoot is None:
            return None
        self.string += myRoot.name + " -> "
        if len(myRoot.nexts) == 0:
            return None
        for next in myRoot.nexts:
            self._populateString(next)
        return



class FolderNode:
    nexts = []
    name = ""

    def __init__(self, name):
        self.name = name
        self.nexts = []
        return
    
    def createFolder(self, name):
        myFolder = FolderNode(name)
        self.nexts.append(myFolder)
        return

directory = Tree()
directory.root.createFolder("first")
directory.root.createFolder("second")
directory.printFolders()