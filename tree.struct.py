class Tree:
    root = None
    string = ""
    def __init__(self):
        self.root = FolderNode("LocalDisk")
        self.string = ""
        return

    # A Public access member method to find the required folder
    def getFolder(self, folderName):
        return self._folderSearch(self.root, folderName)
    
    # A Helper private member method to find the required folder that requires the root as well as the folder name
    def _folderSearch(self, root, folderName):
        if root is None:
            return root
        
        if root.name == folderName:
            return root
        folder = None
        for next in root.nexts:
            folder = self._folderSearch(next, folderName)
            if folder:
                return folder
        return folder

    # A public member method to get the children folders/files of the folder passed in
    def getFolderChildren(self, folder):
        return folder.getChildren()

    # A public member method to print all the folders
    def printFolders(self):
        self._populateString(self.root)
        print(self.string)
        self.string = ""
        return
    # A public member method to print all the nested children folder names including the parent folder
    def printFolderChildrens(self, folder):
        self._populateString(folder)
        print(self.string)
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
    
    def getChildren(self):
        return self.nexts

# ----------------- TESTING METHODS BELOW --------------------

directory = Tree()
directory.root.createFolder("first")
directory.root.createFolder("second")

folder = directory.getFolder("first")

directory.printFolderChildrens(folder)
# print(folder.name if folder else "Folder Not Found!")

# directory.printFolders()

# ------------------ TEST ENDS HERE ---------------------------