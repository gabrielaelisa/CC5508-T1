import matplotlib.pyplot as plt
from skimage import io

class Image:
    def __init__(self, file):
        self.filename = file
        self.image = io.imread(self.filename)

    def display(self):
        fig, xs = plt.subplots(1,1)
        xs.set_axis_off()
        xs.imshow(self.image)
        xs.set_title("Image")
        plt.show()

    def to_gray(self):
        # GRAY = 0.299*ROJO + 0.587*VERDE + 0.114*AZUL

        red = self.image[:, :, 0]
        green = self.image[:, :, 1]
        blue = self.image[:, :, 2]

        grey = 0.299 * red + 0.587 * green + 0.114 * blue
        self.image= grey
Image('ejemplos/rut_2.jpg').display()
