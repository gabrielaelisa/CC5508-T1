from GreyImage import *
class Character(GreyImage):
    def __init__(self, name, file, algorithm):

        '''
        :param file: source file jpg image
        :param name: character name (number or letter) 1, 2.. 9 or k
        '''
        self.name= name
        self.gimage= io.imread(file)
        super().__init__(self.gimage, algorithm)
        self.feature_vector= self.components[0].feature_vector