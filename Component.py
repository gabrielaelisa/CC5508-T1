import math
import numpy as np

class Component:

    def __init__(self, id):
        # points that form the component
        self.id = id
        self.points = []
        self.boundary = []
        self.boundingbox = []
        self.feature_vector = []
        self.proportion= 0

    def init_attributes(self, image):
        self.find_box()
        self.find_borders(image)
        self.find_fv()
        self.proportion=len(self.boundary)/self.boundingbox[2]*self.boundingbox[3]

    def append_point(self, x):
        '''

        :param x: tuple (i,j)
        :return: void
        '''
        self.points.append(x)

    def find_box(self):
        x_min = self.points[0][0]
        x_max = x_min
        y_min = self.points[0][1]
        y_max = y_min
        for (x, y) in self.points:
            if x < x_min:
                x_min = x
            if x > x_max:
                x_max = x
            if y < y_min:
                y_min = y
            if y > y_max:
                y_max = y
        # initialpoint for bondingbox
        # esquina superior izquierda
        # todo
        # checkear que este dentro de los indices de la imagen
        xi = x_min - 1
        yi = y_max + 1
        width = x_max + 1 - (x_min - 1)
        heigth = y_max + 1 - (y_min - 1)
        self.boundingbox.extend([xi, yi, width, heigth])

    def draw_box(self, image):
        box = self.boundingbox
        red = image[:, :, 0]
        green = image[:, :, 1]
        blue = image[:, :, 2]
        x = box[0]
        y = box[1]
        w = box[2]
        h = box[3]

        for i in range(x, x + w + 1):
            # borde superior
            red[i][y] = 255
            green[i][y] = blue[i][y] = 0
            # borde inferior
            red[i][y - h] = 255
            green[i][y - h] = blue[i][y - h] = 0
        for j in range(y - h, y + 1):
            # borde izquiedo
            red[x][j] = 255
            green[x][j] = blue[x][j] = 0
            # borde derecho
            red[x + w][j] = 255
            green[x + w][j] = blue[x + w][j] = 0

    def in_range(self, x, im):
        '''

        :param x: tuple (i,j)
        :param im: image matrix
        :return: bool , is the tuple inside the range of the graph limits
        '''
        if x[0] < len(im) and x[0] >= 0:
            return x[1] < len(im[0])  and x[1] >= 0

    def next_neighbour(self, p, q):
        '''
        returns point q next clockwise neighbour,
        starting from q
        :param p: black point (0)
        :param q: white neighbour point (1)
        :return: next point q
        '''
        #todo checkear que no se sale de los bordes de la imagen
        i = p[0]
        j = p[1]
        n = [(i, j - 1), (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
             (i, j + 1), (i + 1, j + 1), (i + 1, j), (i + 1, j - 1)]
        indx = n.index(q)
        if indx == len(n) - 1:
            return n[0]
        else:
            return n[indx + 1]

    def find_borders(self, image):
        d = 100000
        p0 = (0, 0)
        '''
        i_0= self.boundingbox[0]
        j_0= self.boundingbox[1]
        for row in range()
        '''

        '''look for the point with smaller euclidean distance from de origin
        this point will be the start point'''
        for x in self.points:
            dist = math.sqrt(math.pow(x[0], 2) + math.pow(x[1], 2))
            if dist < d:
                d = dist
                p0 = (x[0], x[1])

        p = p0
        q = (p0[0], p0[1] - 1)

        self.boundary.append(p)

        while (self.next_neighbour(p, q) != p0):
            q_p = q
            q = self.next_neighbour(p, q_p)
            if (not self.in_range(q,image) or not image[q[0]][q[1]]):
                p = q
                q = q_p
                self.boundary.append(p)

    def draw_borders(self, image):
        """
        :param image: rgb image
        :return: void
        """
        red = image[:, :, 0]
        green = image[:, :, 1]
        blue = image[:, :, 2]
        for x in self.boundary:
            i = x[0]
            j = x[1]
            if self.boundary.index(x)==0:
                red[i][j] = 0
                green[i][j] = blue[i][j] = 255
            else:

                # borde superior
                red[i][j] = 255
                green[i][j] = blue[i][j] = 0


    def find_fv(self):
        heigth= self.boundingbox[2]/2
        width= self.boundingbox[3]/3
        TOP=[]
        BTM= []
        LFT= []
        RGT= []
        for point in self.boundary:
            if point[0]> heigth:
                TOP.append(point)
            else: BTM.append(point)
        for point in self.boundary:
            if point[1]> width:
                RGT.append(point)
            else: LFT.append(point)


        ''' key direction, value indx 
        up, down , left, right ,t-left,t-right, bot-l, bot-r
        '''
        keys = {(-1, 0): 0, (1, 0): 1, (0, -1): 2, (0, 1): 3,
                (-1, -1): 4, (-1, 1): 5, (1, -1): 6, (1, 1): 7}

        # feature vector
        FV = [0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0]
        for x in (TOP, BTM, LFT, RGT):
            u=0
            for i in range(len(x)-1):
                prev = x[i]
                next = x[i + 1]
                diff = np.subtract(next, prev)
                key = (diff[0], diff[1])
                if keys.__contains__(key):
                    indx = keys[key]
                    FV[indx +u*8] += 1
            u+=1
        magnitude= math.sqrt(sum(FV[i] * FV[i] for i in range(len(FV))))
        self.feature_vector= np.true_divide(FV, magnitude)





