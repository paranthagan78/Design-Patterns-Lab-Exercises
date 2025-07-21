from abc import ABC, abstractmethod

# Component Interface
class FileSystemComponent(ABC): 
    @abstractmethod
    def display(self):
        pass

# Leaf
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"File: {self.name}")

# Composite
class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self):
        print(f"Directory: {self.name}")
        for child in self.children:
            child.display()

# Client Code
if __name__ == "__main__":
    file1 = File("file1.txt")
    file2 = File("file2.txt")

    directory1 = Directory("Folder 1")
    directory1.add(file1)

    directory2 = Directory("Folder 2")
    directory2.add(file2)

    root_directory = Directory("Root")
    root_directory.add(directory1)
    root_directory.add(directory2)

    # Displaying the file system structure
    root_directory.display()
    
"""
from abc import ABC, abstractmethod

class FileComponent(ABC):
    @abstractmethod
    def display(self):
        pass
class File(FileComponent):
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"File Name: {self.name}")
class Folder(FileComponent):
    def __init__(self,name):
        self.name=name
        self.children=[]
    def add(self,children):
        self.children.append(children)
    def remove(self,children):
        self.children.remove(children)
    def display(self):
        print(f"Folder: {self.name}")
        for child in self.children:
            child.display()

f1=File('f1.txt')
f2=File('f2.txt')
f3=File('f3.txt')
f4=File('f4.txt')
d1=Folder('Folder1')
d2=Folder('Folder2')
root=Folder('Root')
d1.add(f1)
d1.add(f2)
d2.add(f1)
d2.add(f2)
d2.add(f3)
d2.add(f4)
d1.display()
d2.display()
print("*"*50)
d2.remove(f1)
d2.remove(f2)
d1.display()
d2.display()
print("*"*50)
root.add(d1)
root.add(d2)
root.display()
"""