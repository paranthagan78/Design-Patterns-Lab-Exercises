class Node:

    '''creating a class node '''

    def __init__(self, item = None, prev = None, next = None , parent =  None) :

        self.item = item
        self.left = prev
        self.right = next
        self.parent = parent

class Tree() :

    '''creating a tree data structure to perform operation like insert , search , delete and traverse operations'''

    def __init__(self) :
        self.root = None
        self.size = 0

    def left (self,pos) :
        return pos.left

    def right(self ,pos):
        return pos.right
    
    def addroot(self,item) :                                                  # creates the root of the tree
        if self.root is not None :
            raise ValueError("root exits")
        root = Node(item)
        self.size = 1
        return root

    def addleft(self,item,pos) :                                           # add the left node to the node by creating a new node with item
        
        if pos is None:
            raise TypeError('Not a valid position.')
        if self.left(pos) is not None :
            raise ValueError("item is there")
        else:
            pos.left = Node(item,parent = pos)
            self.size += 1
            return pos.left
        
    def addright(self,item,pos) :                                          # add the right node to the node by creating a new node with item

        if pos is None:
            raise TypeError('Not a valid position.')
        if self.right(pos) is not None :
            raise ValueError("item is there")
        else:
            pos.right = Node(item,parent = pos)
            self.size += 1
            return pos.right

    def parent(self,pos) :
        return pos.parent
    
    def insert(self,element,pos) :                                             # insert the element in the tree
                    
        if pos == None:
            self.root = self.addroot(element)
        
        while pos is not None:
            if pos.item > element :
                if pos.left is None :
                    self.addleft(element,pos)
                    break
                else :
                    return (self.insert(element, pos.left))
            else :
                if pos.right is None :
                    self.addright(element,pos)
                    break
                else :
                    return (self.insert(element,pos.right)) 
    
    def search(self,element,pos) :                                       # search the elrement in the tree

        if pos.item == element:
            return True
        elif pos.item > element :
           return (self.search(element, pos.left))
        elif pos.item < element :
                return (self.search(element,pos.right)) 
        else :
            return False

    def address(self,element,pos) :                                       # search the elrement in the tree

        if pos.item == element:
            return pos
        elif pos.item > element :
           return (self.address(element, pos.left))
        elif pos.item < element :
                return (self.address(element,pos.right)) 
        else :
            return None

    def findmin (self,pos) :                                              # returns the mininum element of the tree
        if pos.left is None : 
            return pos
        else :
            return self.findmin(pos.left)


    def delete (self,element) :

        pos = self.address(element,self.root)
        Parent = self.parent(pos)
        
        if pos.left == None and pos.right == None :                                        # delete the node which has no child
            if Parent.left == pos :
                Parent.left = None
                self.size -= 1
            elif Parent.right == pos :
                Parent.right = None
                self.size -= 1
                
        elif pos.left != None and pos.right == None :                                     # delete the node which has left child alone
            if Parent.left == pos : 
                Parent.left = pos.left
                self.size -= 1
            else:
                Parent.right = pos.left
                self.size -= 1
                
        elif pos.left == None and pos.right != None :                                     # delete the node which has right child alone
            if Parent.left == pos :
                Parent.left = pos.right
                self.size -= 1
            else:
                Parent.right = pos.right
                self.size -= 1
                
        elif pos.left != None and pos.right != None :                                    # delete the node which has two child
            r = self.findmin(pos.right)
            pos.item = r.item
            r.item = 20000000
            self.delete(r.item)
        

    def traverse(self,pos):

        if pos is None :
            pos = self.root
        if pos is not None :
            if pos.left is not None :
                self.traverse(pos.left)  
            print(pos.item)
            if pos.right is not None :
                self.traverse(pos.right) 

'''a = Tree()
a.insert(6,a.root)
a.insert(5,a.root)
a.insert(8,a.root)
a.traverse(a.root)
print(a.search(5,a.root))
a.delete(6)
a.traverse(a.root)'''
