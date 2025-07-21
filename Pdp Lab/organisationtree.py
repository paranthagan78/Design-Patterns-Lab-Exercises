from inheritanceTREE import Tree

class OrganisationTree (Tree):
    
    '''This subclass simulate a organisational hierarchy where each node represents an employee or department .'''
    
    def add(self,element ,pos) :                                                                # add the employees or departments in the tree
        super().insert(element ,pos)
        
    def search_employee (self, element ,pos,position) :
        ''' search for a employee if he/she is present ,then return "true "or else return "false"
        if the other than employee is given as input ,then it return "not an employee" '''
                                                                                                 
        if position == "employee" :
            return super().search(element ,pos)
        else:
            print("not an employee")
            
    def display(self,x):                                                                       # display the employees or department
        super().traverse(x)
        
    '''def delete(self,item):                                                                  # delete the employees or department
        super().delete(item)'''
        
if __name__ == '__main__' :
    
    # creating a instance for child class    
    a = OrganisationTree()
    
    # add the employees and departments
    a.add("maths",a.root)
    a.add("Vignesh",a.root)
    a.add("IT",a.root)
    
    # displaying the employees and departments
    a.display(a.root)
    
    # search an employee
    print(a.search_employee("Vignesh",a.root,"employee"))
    
    a.search_employee("maths",a.root,"department")
    
    # delete an employee or departments
    a.delete("IT")
    
    # display the final list after a deletion
    a.display(a.root)