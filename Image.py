import matplotlib.pyplot as plt
from skimage import io
from Algorithms import *
from Graph import *

class Image:

    def __init__(self, file, algorithm):
        '''

        :param file: source file jpg image
        :param algorithm: funcition either Otsu or Adaptative
        '''
        self.filename = file
        self.rgbimage = io.imread(self.filename)
        self.gimage = self.to_gray()
        self.binimage = self.to_binary(algorithm)
        self.components = self.get_components()
        self.init_attributes()

    def init_attributes(self):
        for x in self.components:
            x.init_attributes()

    def display(self, color):
        '''

        :return: shows a grafic of the image
        '''
        map = {'gray': (self.gimage, 255), 'color': (self.rgbimage, 255), 'binary': (self.binimage, 1)}
        val = map.get(color)
        fig, xs = plt.subplots(1, 1)
        xs.set_axis_off()
        xs.imshow(val[0], cmap="gray", vmin=0, vmax=val[1])
        xs.set_title(color +" " + "Image")
        plt.show()

    def get_histogram(self):
        '''

        :return: histogram of an image
        the number of ocurrences of each value
        '''
        h = np.zeros(256, dtype=np.float32)
        for i in range(self.gimage.shape[0]):
            for j in range(self.gimage.shape[1]):
                gcolor = int(self.gimage[i, j])
                h[gcolor] += 1.0
        return h

    def to_gray(self):
        '''

        :return: process a 3 channesl RGB image and returns a 1 channel
        grey image
        '''
        # GRAY = 0.299*ROJO + 0.587*VERDE + 0.114*AZUL
        red = self.rgbimage[:, :, 0]
        green = self.rgbimage[:, :, 1]
        blue = self.rgbimage[:, :, 2]
        gray = 0.299 * red + 0.587 * green + 0.114 * blue
        return gray

    def to_binary(self, algorithm):
        '''

        :param algorithm: Otsu or adaptative algorithm
        for thresholf
        :return: returns image in binary form
        '''
        th = algorithm(self)
        # correctly should be 1
        # 255 only for visuals
        mybin = self.gimage >= th
        print(mybin)
        return mybin

    def get_components(self):
        '''

        :return: list of Components  for values
        marked as '0'
        '''
        g = Graph(self.binimage)
        g.dfs()

        return g.components

    def draw_box(self):
        image = self.rgbimage
        l = len(self.components)
        sum = 0

        for x in self.components:
            sum += x.boundingbox[2] * x.boundingbox[3]
        average = sum / l
        for x in self.components:
            if (x.boundingbox[2] * x.boundingbox[3] > 2 / 3 * average):
                x.draw_box(image)

    def draw_border(self):
        for x in self.components:
            x.find_borders(self.binimage)
            x.draw_borders(self.rgbimage)


#imagen = Image('ejemplos/rut_2.jpg', Adaptative)
#imagen.display("binary")
