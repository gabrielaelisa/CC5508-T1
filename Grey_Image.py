import matplotlib.pyplot as plt
from skimage import io
from Algorithms import *

class Grey_Image:
    def __init__(self, file):
        self.filename = file
        self.rgbimage = io.imread(self.filename)
        self.image= self.to_gray()



    def display(self):
        fig, xs = plt.subplots(1,1)
        xs.set_axis_off()
        xs.imshow(self.image, cmap="gray", vmin=0, vmax=255)
        xs.set_title("Image")
        plt.show()

    ''' get histogram of an image
    the number of ocurrences of each value'''

    def get_histogram(self):
        h = np.zeros(256, dtype=np.float32)
        for i in range(self.image.shape[0]):
            for j in range(self.image.shape[1]):
                gcolor= int(self.image[i, j])
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
        grey = 0.299 * red + 0.587 * green + 0.114 * blue
        return grey

    def to_binary(self, algorithm):
        th = algorithm(self)
        print(th)
        bin_im = np.zeros(self.image.shape, np.uint8)
        # correctly should be 1
        # 255 only for visuals
        bin_im[self.image >= th] = 255
        print(bin_im)
        self.image= bin_im

imagen=Grey_Image('ejemplos/rut_2.jpg')
imagen.to_binary(getOtsu)
imagen.display()
