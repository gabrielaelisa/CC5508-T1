
class Component:

    def __init__(self,id):
        # points that form the component
        self.id= id
        self.points= []
        self.boundary= []
        self.boundingbox= []

    def append_point(self, x):
        '''

        :param x: tuple (i,j)
        :return: void
        '''
        self.points.append(x)

    def find_box(self):
        x_min =self.points[0][0]
        x_max= x_min
        y_min= self.points[0][1]
        y_max= y_min
        for (x,y) in self.points:
            if x<x_min:
                x_min= x
            if x>x_max:
                x_max=x
            if y< y_min:
                y_min=y
            if y> y_max:
                y_max=y
        # initialpoint for bondingbox
        # esquina superior derecha
        # todo
        # checkear que este dentro de los indices de la imagen
        xi = x_min-1
        yi= y_max +1
        width= x_max +1 -(x_min-1)
        heigth= y_max +1 -(y_min -1)
        self.boundingbox.extend([xi, yi, width, heigth])
        print(self.boundingbox)

com = Component(1)
com.points= [(1,2),(2,3),(3,4),(4,5)]
com.find_box()


