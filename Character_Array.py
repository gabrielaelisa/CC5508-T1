import os
from Character import *
class Characters:
    def __init__(self,path, algorithm):
        '''

        :param path: directory path for each character
        :param algorithm: otsu or adaptative
        '''
        #list of characters containing a list of each photo example
        self.chars=[[],[],[],[],[],[],[],[],[],[]]

        for subdir, dirs, files in os.walk('modelos'):
            for file in files:
                name= os.path.split(subdir)[1]
                if name =='K':
                    continue
                else:
                    self.chars[int(name)].append(Character(name, os.path.join(subdir, file), algorithm))

                print(os.path.join(subdir, file))
        '''
        subdirs=  [x[0] for x in os.walk('modelos/')]
        subdirs.pop(0)
        for dir in subdirs
        print(subdirs)
        for subdir in os.walk('modelos/'):
            for x in subdir:
                print(x)
            #for file in subdir:
        '''

c = Characters('hola', Otsu)