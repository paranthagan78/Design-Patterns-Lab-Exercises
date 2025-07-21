from inheritanceTREE import Tree
import os

class FilesSystemTree(Tree):
    
    '''This subclass simulate a file system hierarchy where each node represents a directory or file .'''
    
    def search_file (self, element ,pos) :
        ''' search for a file if it is present ,then return "true "or else return "false"
        if the other than file is given as input ,then it return "it is not a file" '''
                                                                                                 
        if os.path.isfile(element):
            return super().search(element ,pos)
        else:
            print("It is not a file")
        
    def add(self,element ,pos) :                                                                
        super().insert(element ,pos)
        
    def display(self,x):                                                                     
        super().traverse(x)
    
if __name__ == '__main__' :        
    
      
    a = FilesSystemTree()
    
    # add the files and directories
    a.add("C:\Users\marim\OneDrive\Documents\sem-3\DESIGN PATTERN\Madhusudhanan-UIT2311-ex-03\filessystemtree.py",a.root)
    a.add("C:\Users\marim\OneDrive\Documents\sem-3\DESIGN PATTERN\Madhusudhanan-UIT2311-ex-02\library.py",a.root)
    a.add("E:\it lab\SEM 3\Programming and Design Patterns\Lab\library.py",a.root)
    
    a.display(a.root)
    
    # search a file
    print(a.search_file("C:\Users\marim\OneDrive\Documents\sem-3\DESIGN PATTERN\Madhusudhanan-UIT2311-ex-07\Ques-1.py",a.root))
    
    a.search_file("C:\Users\marim\OneDrive\Documents\sem-3\DESIGN PATTERN\Madhusudhanan-UIT2311-ex-06\calculator.py",a.root)                      # output : It is not a file
    
    # delete a file or directory
    a.delete("E:\it lab\SEM 3\Programming and Design Patterns\Lab")
    
    # display the final list after a deletion
    a.display(a.root)
    