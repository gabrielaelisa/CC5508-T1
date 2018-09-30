from Component import *
import queue
import matplotlib.pyplot as plt


class Graph:

    def __init__(self, matrix):
        self.M = matrix
        self.rows = len(self.M)
        self.cols = len(self.M[0])
        # vector of visited nodes
        self.V = []
        # vector of 8-connected componets
        self.components = []
        # current component id
        self.id = 0

    def mark_visited(self, x):
        '''

        :param x: tuple (i,j) for position of a node in a graph
        :return: void
        '''
        self.V.append(x)

    def in_range(self, x):
        '''

        :param x: tuple (i,j)
        :return: bool , is the tuple inside the range of the graph limits
        '''
        if x[0] < self.rows and x[0] >= 0:
            return x[1] < self.cols and x[1] >= 0

    # my depth search algorithm
    def dfs(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) in self.V: continue
                self.mark_visited((i, j))
                # print(i,j)
                if (self.M[i][j] == 0):
                    comp = Component(self.id)
                    self.components.append(comp)
                    comp.append_point((i, j))
                    self.id += 1
                    self.bfs_iterative(comp, i, j)

    # my breadth search algorithm
    def bfs_iterative(self, comp, i, j):
        '''

        :param comp: Component
        :param i: position in row
        :param j: position in column
        :return: void
        '''
        myqueue = queue.Queue(maxsize=0)
        myqueue.put((i, j))
        while not myqueue.empty():
            x = myqueue.get()
            i = x[0]
            j = x[1]
            neighbours = [(i - 1, j), (i - 1, j + 1), (i, j + 1), (i + 1, j + 1),
                          (i + 1, j), (i + 1, j - 1), (i, j - 1), (i - 1, j - 1)]
            for x in neighbours:
                if self.in_range(x) and x not in self.V:

                    if self.M[x[0]][x[1]] == 0:
                        self.mark_visited(x)
                        comp.append_point(x)
                        myqueue.put(x)
