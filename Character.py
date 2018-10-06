from Image import*
class Character(Image):
    def __init__(self, name):
        '''

        :param name: character name (number or letter) 1, 2.. 9 or k
        '''
        self.name= name
