import matplotlib.pyplot as plt
from skimage import io
from Algorithms import *
from Component import *
import queue


class GreyImage:

    def __init__(self, grey_image, algorithm):
        '''

        :param gray_image: 1 channel matrix of max value 255
        :param algorithm: function either Otsu or Adaptative
        '''
        self.image = grey_image
        self.binimage = self.to_binary(algorithm)
        # vector of 8-connected componets
        self.components = []
        # -----------------------------------------

        self.rows = len(self.binimage)
        self.cols = len(self.binimage[0])
        # vector of visited nodes
        self.V = []
        # current component id
        self.id = 0
        self.init_attributes()

    def init_attributes(self):
        self.dfs()
        for x in self.components:
            x.init_attributes(self.binimage)
        self.reorder_components()
        self.select_components()

    def reorder_components(self):
        s = sorted(self.components, key=lambda x: x.boundingbox[0])
        self.components = s

    def select_components(self):
        avrg= self.avrg_size()
        new_components=[]
        for c in self.components:
            if c.proportion> 2/3*avrg:
                new_components.append(c)
        self.components=new_components

    def get_histogram(self):
        '''

        :return: histogram of an image
        the number of ocurrences of each value
        '''
        h = np.zeros(256, dtype=np.float32)
        for i in range(self.image.shape[0]):
            for j in range(self.image.shape[1]):
                gcolor = int(self.image[i, j])
                h[gcolor] += 1.0
        return h

    def to_binary(self, algorithm):
        '''

        :param algorithm: Otsu or adaptative algorithm
        for thresholf
        :return: returns image in binary form
        '''
        th = algorithm(self)
        # correctly should be 1
        # 255 only for visuals
        mybin = self.image >= th
        return mybin

    def avrg_size(self):
        l = len(self.components)
        sum = 0

        for x in self.components:
            sum += x.proportion
        return sum / l


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
                if (self.binimage[i][j] == 0):
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

                    if self.binimage[x[0]][x[1]] == 0:
                        self.mark_visited(x)
                        comp.append_point(x)
                        myqueue.put(x)
