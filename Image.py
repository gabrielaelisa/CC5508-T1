
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
        image = self.rgbimage
        for x in self.components:
            if (x.boundingbox[2] * x.boundingbox[3] > 2 / 3 * self.avrg_size()):
                x.draw_box(image)

    def draw_border(self):
        for x in self.components:
            if (x.boundingbox[2] * x.boundingbox[3] > 2 / 3 * self.avrg_size()):
                x.draw_borders(self.rgbimage)


imagen = Image('ejemplos/rut_7.jpg', Otsu)
imagen2=Character(6,'modelos/6/6_1.jpg', Adaptative)
imagen.draw_border()

fig, xs = plt.subplots(2, 1)
xs[0].imshow(imagen.rgbimage, cmap='gray', vmax=255, vmin=0)
xs[0].axis('off')
xs[0].set_title("Borders for Adaptative ")

xs[1].imshow(imagen2.binimage, cmap='gray', vmax=1, vmin=0)
xs[1].axis('off')
xs[1].set_title("Borders for Otsu")
'''
xs[2].imshow(image2.binimage, cmap='gray', vmax=1, vmin=0)
xs[2].axis('off')
xs[2].set_title("Adaptative Algorithm")'''
plt.show()
