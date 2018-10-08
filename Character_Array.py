import os
from Character import *
class Characters:
    def __init__(self,algorithm):
        '''

        :param path: directory path for each character
        :param algorithm: otsu or adaptative
        '''
        #list of characters containing a list of each photo example
        self.models=[]

        for subdir, dirs, files in os.walk('modelos'):
            for file in files:
                name= os.path.split(subdir)[1]
                if name =='K':
                    self.models.append(Character(10, os.path.join(subdir, file), algorithm))
                else:
                    self.models.append(Character(int(name), os.path.join(subdir, file), algorithm))
