import matplotlib.pyplot as plt
from skimage import io
from Algorithms import *
from Graph import *
class GreyImage:

    def __init__(self, grey_image, algorithm):
        '''

        :param gray_image: 1 channel matrix of max value 255
        :param algorithm: function either Otsu or Adaptative
        '''
        self.image = grey_image
        self.binimage= self.to_binary(algorithm)
        self.components = self.get_components()
        self.init_attributes()

    def init_attributes(self):
        for x in self.components:
            x.init_attributes(self.binimage)


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

    def get_components(self):
        '''

        :return: list of Components  for values
        marked as '0'
        '''
        g = Graph(self.binimage)
        g.dfs()

        return g.components

    def avrg_size(self):
        l = len(self.components)
        sum = 0

        for x in self.components:
            sum += x.boundingbox[2] * x.boundingbox[3]
        return sum / l

