import sys
from Image import *
from Character_Array import *


def find_best(array):
    sum=[0,0,0,0,0,0,0,0,0,0,0]
    for x in array:
        sum[int(x[1])]+=1

    max = 0
    name = 0
    for i in range(len(sum)):
        if sum[i] > max:
            max = sum[i]
            name = i
    if name == 10:
        return 'k'
    else:
        return name


if __name__ == '__main__':
    map={'otsu': Otsu, 'adaptative': Adaptative}
    file= sys.argv[1]
    th= map.get(sys.argv[2].lower())

    im= Image(file,th)
    box=im.draw_box()
    plt.imsave('boxes.jpg', box)
    border=im.draw_border()
    plt.imsave('borders.jpg', border)
    char=Characters(th)

    for comp in im.components:
        if (comp.boundingbox[2] * comp.boundingbox[3] > 2 / 3 * im.avrg_size()):
            dists= []
            for model in char.models:
                dist= np.linalg.norm(comp.feature_vector - model.feature_vector)
                dists.append((dist, model.name))
            s = sorted(dists, key=lambda x: x[0])
            winners= s[:10]
            print(find_best(winners))


'''
import scipy.misc
#im=io.imread('modelos_nuevos/1/1_nuevo1.jpg')
#print(im)
image= Image('modelos_nuevos/1/1_test.jpg', Adaptative)
im= image.binimage.copy()
scipy.misc.toimage(im, cmin=0, cmax=1).save('modelos/1/1_nuevo2.jpg')


red = image[:, :, 0]
green = image[:, :, 1]
blue = image[:, :, 2]
gray = 0.299 * red + 0.587 * green + 0.114 * blue
scipy.misc.toimage(gray, cmin=0, cmax=255).save('modelos/5/5_nuevo1.jpg')
'''