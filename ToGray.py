import matplotlib.pyplot as plt
from skimage import io

'''
1- channel : process a 3 channesl RGB image and returns a 1 channel
grey image
'''
def one_channel(filename) :
    # GRAY = 0.299*ROJO + 0.587*VERDE + 0.114*AZUL
    image = io.imread(filename)

    red = image[:, :, 0]
    green = image[:, :, 1]
    blue = image[:, :, 2]

    grey= 0.299*red + 0.587*green + 0.114*blue

    fig, xs = plt.subplots(1, 2)
    for i in range(2):
        xs[i].set_axis_off()

    xs[0].imshow(image)
    xs[0].set_title("Image")
    xs[1].imshow(grey, cmap="gray", vmin=0, vmax=255)
    xs[1].set_title("grey")
    plt.show()
one_channel('ejemplos/rut_2.jpg')