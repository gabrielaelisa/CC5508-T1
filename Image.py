
from GreyImage import *
from Character import *

class Image(GreyImage):

    def __init__(self, file, algorithm):
        '''

        :param file: source file jpg image
        :param algorithm: funcition either Otsu or Adaptative
        '''
        self.rgbimage = io.imread(file)
        self.gimage = self.to_gray()
        super().__init__(self.gimage, algorithm)

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

    def draw_box(self):
        #create a local copy of atribute
        image = self.rgbimage.copy()
        for x in self.components:
            x.draw_box(image)
        return image

    def draw_border(self):
        #idem
        image = self.rgbimage.copy()
        for x in self.components:
            if (x.boundingbox[2] * x.boundingbox[3] > 2 / 3 * self.avrg_size()):
                x.draw_borders(image)
        return image

    def print_characters(self, chars):
        for x in self.components:
            x.find_char(chars)

