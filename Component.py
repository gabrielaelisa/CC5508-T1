
class Component:

    def __init__(self,id):
        # points that form the component
        self.id= id
        self.points= []
        self.boundary= []
        self.boundingbox= []

    def append_point(self, x):
        self.points.append(x)