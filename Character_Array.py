import os
from Character import *
class Characters:
    def __init__(self,algorithm):
        '''

        :param path: directory path for each character
        :param algorithm: otsu or adaptative
        '''
        #list of characters containing a list of each photo example
        self.chars=[[],[],[],[],[],[],[],[],[],[],[]]
        self.fv= {}

        for subdir, dirs, files in os.walk('modelos'):
            for file in files:
                name= os.path.split(subdir)[1]
                if name =='K':
                    self.chars[10].append(Character(name, os.path.join(subdir, file), algorithm))
                else:
                    self.chars[int(name)].append(Character(name, os.path.join(subdir, file), algorithm))

        i=0
        for row in self.chars:
            length= len(row)
            #sum= np.zeros(32)
            sum= np.zeros(4)
            for col in row:
                print(len(col.components))
                cm=col.components[0]
                fv= cm.feature_vector2()
                aux= sum.copy()
                sum=np.add(aux,fv)
            self.fv.update({i: np.true_divide(sum,length)})
            i += 1






c = Characters( Otsu)