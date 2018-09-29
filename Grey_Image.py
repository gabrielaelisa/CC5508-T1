import matplotlib.pyplot as plt
from skimage import io
from Algorithms import *
from Graph import *

#
class Grey_Image:
    def __init__(self, file, algorithm):
        self.filename = file
        self.rgbimage = io.imread(self.filename)
        self.gimage= self.to_gray()
        self.max = 255
        self.binimage= self.to_binary(algorithm)
        self.components = self.get_components()

    '''
    display: shows a grafic of the image
    '''
    def display(self):

        fig, xs = plt.subplots(1,1)
        xs.set_axis_off()
        xs.imshow(self.binimage, cmap="gray", vmin=0, vmax= self.max)
        xs.set_title("Image")
        plt.show()

    ''' get histogram of an image
    the number of ocurrences of each value'''

    def get_histogram(self):
        h = np.zeros(256, dtype=np.float32)
        for i in range(self.gimage.shape[0]):
            for j in range(self.gimage.shape[1]):
                gcolor= int(self.gimage[i, j])
                h[gcolor] += 1.0
        return h

    '''
    to_gray: process a 3 channesl RGB image and returns a 1 channel
    grey image
    '''
    def to_gray(self):
        # GRAY = 0.299*ROJO + 0.587*VERDE + 0.114*AZUL
        red = self.rgbimage[:, :, 0]
        green = self.rgbimage[:, :, 1]
        blue = self.rgbimage[:, :, 2]
        gray = 0.299 * red + 0.587 * green + 0.114 * blue
        return gray

    def to_binary(self, algorithm):
        th = algorithm(self)
        # print(th)
        bin_im = np.zeros(self.gimage.shape, np.uint8)
        # correctly should be 1
        # 255 only for visuals
        mybin= self.gimage >=th
        self.max = 1
        print(mybin)
        return mybin

    def get_components(self):
        g= Graph(self.binimage)
        g.dfs()
        return g.components

imagen=Grey_Image('ejemplos/rut_2.jpg', Adaptative)
imagen.display()
#imagen.display()
