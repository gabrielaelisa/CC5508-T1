import math

class Component:

    def __init__(self,id):
        # points that form the component
        self.id= id
        self.points= []
        self.boundary= []
        self.boundingbox= []

    def init_attributes(self):
        self.find_box()

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
        # esquina superior izquierda
        # todo
        # checkear que este dentro de los indices de la imagen
        xi = x_min-1
        yi= y_max +1
        width= x_max +1 -(x_min-1)
        heigth= y_max +1 -(y_min -1)
        self.boundingbox.extend([xi, yi, width, heigth])

    def draw_box(self, image):
        box= self.boundingbox
        red = image[:, :, 0]
        green = image[:, :, 1]
        blue = image[:, :, 2]
        x = box[0]
        y= box[1]
        w= box[2]
        h= box[3]

        for i in range(x, x+w+1):
            #borde superior
            red[i][y]= 255
            green[i][y]=blue[i][y]= 0
            #borde inferior
            red[i][y-h] = 255
            green[i][y-h] = blue[i][y-h] = 0
        for j in range(y-h , y+1):
            #borde izquiedo
            red[x][j] = 255
            green[x][j] = blue[x][j] = 0
            #borde derecho
            red[x+w][j] = 255
            green[x+w][j] = blue[x+w][j] = 0

    def next_neighbour(self, p, q):
        '''
        returns point p next clockwise neighbour,
        starting from q
        :param p:
        :param q:
        :return:
        '''
        i= p[0]
        j= p[1]
        n= [(i, j-1), (i-1, j-1), (i-1, j), (i-1,j+ 1),
            (i, j+1), (i+1, j+1), (i+1, j), (i+1, j-1)]
        indx= n.index(q)
        if indx==len(n)-1:
            return n[0]
        else:
            return n[indx+1]

    def find_borders(self, image):
        d= 100000
        p0= (0,0)

        #look for the point with smaller euclidean distance from de origin
        #this point will be the start poiny
        for x in self.points:
            dist= math.sqrt(math.pow(x[0],2)+ math.pow(x[1],2))
            if dist<d:
                d=dist
                p0= (x[0], x[1])
        p=p0
        self.boundary.append(p)
        #previous
        q= (p0[0],p0[1]-1)
        #next
        n= q
        while (n!=p0):
            qo=q
            q=n
            n=self.next_neighbour(p,qo)
            if(image[n[0]][n[1]]):
                p=n
                self.boundary.append(p)
            #else:
            #   q=n



    def draw_borders(self, image):
        red = image[:, :, 0]
        green = image[:, :, 1]
        blue = image[:, :, 2]
        for x in self.boundary:
            i= x[0]
            j= x[1]
            # borde superior
            red[i][j] = 255
            green[i][j] = blue[i][j] = 0





#com = Component(1)
#com.points= [(1,2),(2,3),(3,4),(4,5)]
#com.find_box()


