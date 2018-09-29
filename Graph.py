from Component import *

class Graph():

    def __init__(self, matrix):
        self.M = matrix
        self.rows= len(self.M)
        self.cols= len(self.M[0])
        #vector of visited nodes
        self.V= []
        # vector of 8-connected componets
        self.components= []
        # current component id
        self.id = 0

    def mark_visited(self, x):
        self.V.append(x)


    # my depth search algorithm
    def dfs(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if (i,j) in self.V: continue
                self.mark_visited((i,j))
                #print(i,j)
                if(self.M[i][j]==1):
                    comp= Component(self.id)
                    self.components.append(comp)
                    self.id += 1
                    self.bfs(comp,i,j)

    def in_range(self, x):
        if x[0]< self.rows and x[0]>=0:
            return x[1]< self.cols and x[1]>=0

    # my breadth search algorithm
    def bfs(self,comp, i,j):
        # 8-connect neighbours
        neighbours=[(i-1,j), (i-1, j+1), (i, j+1), (i+1, j+1),
                    (i+1, j), (i+1, j-1), (i, j-1), (i-1, j-1)]
        for x in neighbours:
            if self.in_range(x) and x not in self.V:
                self.mark_visited(x)
                if self.M[x[0]][x[1]] ==1:
                    comp.append_point(x)
                    self.bfs(comp, x[0], x[1])






m = Graph([[2, 1],[ 3, 4]])
m.dfs()