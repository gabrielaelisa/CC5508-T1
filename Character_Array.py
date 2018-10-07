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
        self.fv= {}

        for subdir, dirs, files in os.walk('modelos'):
            for file in files:
                name= os.path.split(subdir)[1]
                if name =='K':
                    continue
                else:
                    self.chars[int(name)].append(Character(name, os.path.join(subdir, file), algorithm))

                #print(os.path.join(subdir, file))

        for row in self.chars:
            i=0
            for col in row:
                i+=1
                cm=col.components[0]
                fv= cm.feature_vector()






c = Characters('hola', Otsu)