import sys
from Image import *
from Character_Array import *
if __name__ == '__main__':
    map={'otsu': Otsu, 'adaptative': Adaptative}
    file= sys.argv[1]
    th= map.get(sys.argv[2].lower())
    im= Image(file,th)
    box=im.draw_box()
    im.draw_border()
    plt.imsave('bordes.jpg', box )
    char= Characters(th)
    im.print_characters(char)


