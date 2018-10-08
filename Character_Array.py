import os
from Character import *
class Characters:
    def __init__(self,algorithm):
        '''

        :param path: directory path for each character
        :param algorithm: otsu or adaptative
        '''
        #list of characters containing a list of each photo example
        self.chars=[[],[],[],[],[],[],[],[],[],[]]
        self.fv= {}

        for subdir, dirs, files in os.walk('modelos_nuevos'):
            for file in files:
                name= os.path.split(subdir)[1]
                if name =='K':
                    continue
                    self.chars[10].append(Character(name, os.path.join(subdir, file), algorithm))
                else:
                    self.chars[int(name)].append(Character(name, os.path.join(subdir, file), algorithm))

    def round(self,i):
        indx=0
        for row in self.chars:
            #print(row[i].name)
            col = row[i]
            cm = col.components[0]
            fv = cm.feature_vector()
            self.fv.update({indx: fv})
            indx+=1



c = Characters( Otsu)