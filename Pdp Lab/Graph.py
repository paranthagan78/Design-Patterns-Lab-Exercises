# -*- coding: utf-8 -*-


'''
The following comprises of code for finding efficient water pipeline
network to connect all the cities with a minimal cost using a minimum
spanning tree in a graph ADT. This is a part of the excercises given
under UIT2312 - Programming and Design Patterns.

It will return the minimum cost as well as the path connecting each
city and check water availability based on the demand.

I have followed good coding practices.

Author : <madhusudhanan2210528@ssn.edu.in>
Register number : 3122 22 5002 067

'''


import sys


class Coords:

    '''
    This class is used for creating coordinates and finding distance
    between two coordinates and display the given coordinates.

    Methods:
        __init__ : The constructor.
        dist : Finds the distance between two Coords objects.
        __str__ : Returns a string object of the Coords object.
    
    '''

    def __init__(self,x,y):

        self.x = x
        self.y = y
    
    def dist(self,other):

        s = (self.x - other.x)**2 + (self.y - other.y)**2
        return s**0.5

    def __str__(self):

        return '(' + str(self.x) + ',' + str(self.y) + ')'


class Graph:

    '''
    The following class contains a graph ADT implementation which allows
    us to find the minimum spanning tree and thus find the minimum cost
    required to lay pipelines.

    Methods:
        __init__ : The constructor.
        min_dist_points : Used to find the minimum distance value
        between the given Coords object and list of Coords objects.
        adjmatrix : Returns the adjacency matrix for all given Coords.
        printval : Returns the required city for a given coordinate
        which is usually printed.
        difference between demand and amount of water available.
        prim_mst : Uses prim to find the minimum spanning tree.
    
    '''

    def __init__(self,d,demand_lst=None):
        
        self.d = d
        lst = [x for x in d.keys()]
        self.lst = lst
        if demand_lst is None:
            demand_lst = [1] * len(lst)
        self.demand_lst = demand_lst

    def min_dist_points(self,a,b):

        mpoint = ''
        mval = a.dist(b[0])
        for i in b:
            if mval < a.dist(b[i]):
                mval = a.dist(b[i])
                mpoint = b[i]
        
        return mpoint

    def adjmatrix(self):

        adjmatrixlist = []
        for i in self.lst:
            sidelst = []
            ct = 0
            for j in self.lst:
                if i != j:
                    sidelst.append(i.dist(j) * self.demand_lst[ct])
                    ct += 1
                else:
                    sidelst.append(0)
            adjmatrixlist.append(sidelst)
        
        return adjmatrixlist

    def printval(self,ind):
        value = self.lst[ind]
        return self.d[value]

    def prim_mst(self):
        adj_matrix = self.adjmatrix()
        n = len(adj_matrix)
        
        parent = [0] * n
        key = [sys.maxsize] * n
        key[0] = 0
        mst_set = [False] * n
        
        for _ in range(n):
            min_key = sys.maxsize
            min_index = -1
            for v in range(n):
                if key[v] < min_key and not mst_set[v]:
                    min_key = key[v]
                    min_index = v
            
            mst_set[min_index] = True
            
            for v in range(n):
                if adj_matrix[min_index][v] and not mst_set[v] and adj_matrix[min_index][v] < key[v]:
                    parent[v] = min_index
                    key[v] = adj_matrix[min_index][v]
    
        total_cost = 0
        dictionary = {}
        for i in range(1, n):
            val1 = a.printval(i)
            val2 = a.printval(parent[i])
            if str(val2) not in dictionary.keys():
                dictionary[str(val2)] = [str(val1)]
            else:
                dictionary[str(val2)].append(str(val1))
            total_cost += adj_matrix[i][parent[i]]
            print(f"Distance between {val1} and {val2}: {adj_matrix[i][parent[i]]}")

        return (total_cost,dictionary)


#driver code
if __name__ == '__main__':
    #The code provided here will not be executed when imported

    p1 = Coords(1,2)
    p2 = Coords(3,4)
    p3 = Coords(5,6)
    p4 = Coords(0,2)
    p5 = Coords(0,0)
    p6 = Coords(1,1)
    d = {p1 : 'Chennai', p2 : 'Chenkalpattu', p3 : 'Kanchipuram', p4 : 'Vellore', p5 : 'Kanyakumari',p6 : 'Madurai'}
    a = Graph(d)
    print()
    

    #printing the shortest distances between each city and path
    minimum_cost,dictpaths = a.prim_mst()
    print()

    #printing total cost of tree
    print("Total cost is :",minimum_cost)
    print()

    #printing all the paths
    print("Paths to each point is :",dictpaths)
    print()