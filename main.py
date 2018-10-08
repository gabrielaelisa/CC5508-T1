import sys
from Image import *
from Character_Array import *
if __name__ == '__main__':
    map={'otsu': Otsu, 'adaptative': Adaptative}
    file= sys.argv[1]
    th= map.get(sys.argv[2].lower())
    im= Image(file,th)
    box=im.draw_box()
    plt.imsave('boxes.jpg', box)
    border=im.draw_border()
    plt.imsave('borders.jpg', border)
    char= Characters(th)
    im.print_characters(char)


