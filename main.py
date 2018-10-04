import sys
from Image import *

if __name__ == '__main__':
    map={'otsu': Otsu, 'adaptative': Adaptative}
    file= sys.argv[1]
    th= map.get(sys.argv[2].lower())
    im= Image(file,th)
    im.display('gray')


