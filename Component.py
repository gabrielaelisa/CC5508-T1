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
        self.image= []

    def init_attributes(self, image):
        self.find_box()
        self.find_borders(image)
        self.find_new_fv()
        self.proportion=self.boundingbox[2]*self.boundingbox[3]

    def append_point(self, x):
        '''

        :param x: tuple (i,j)
        :return: void
        '''
        self.points.append(x)

    def find_box(self):
        #column
        x_min = self.points[0][1]
        x_max = x_min
        #row
        y_min = self.points[0][0]
        y_max = y_min
        for (row, col) in self.points:
            if col < x_min:
                x_min = col
            if col > x_max:
                x_max = col
            if row < y_min:
                y_min = row
            if row > y_max:
                y_max = row
        # initialpoint for bondingbox
        # checkear que este dentro de los indices de la imagen

        # esquina superior izquierda
        xi = x_min - 1
        yi = y_max +1
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

        #borde superior
        for j in range(x, x+w):
            red[y][j] = 255
            green[y][j] = blue[y][j] = 0
            # borde inferior
            red[y - h][j] = 255
            green[y - h][j] = blue[y - h][j] = 0

        for i in range(y - h, y):
            # borde izquiedo
            red[i][x] = 255
            green[i][x] = blue[i][x] = 0
            # borde derecho
            red[i][x+w] = 255
            green[i][x + w] = blue[i][x + w] = 0

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
        self.image= image
        d = 100000
        p0 = (0, 0)

        i_0= self.boundingbox[1]
        j_0= self.boundingbox[0]
        w =self.boundingbox[2]
        h= self.boundingbox[3]
        for row in range(i_0, i_0 - h, -1):
            for col in range(j_0, j_0+w):
                if (row,col) in self.points:
                    p0= (row,col)
                    break


        '''look for the point with smaller euclidean distance from de origin
        this point will be the start point
        for x in self.points:
            dist = math.sqrt(math.pow(x[0], 2) + math.pow(x[1], 2))
            if dist < d:
                d = dist
                p0 = (x[0], x[1])'''

        p = p0
        q = (p0[0], p0[1] - 1)

        self.boundary.append(p)
        if len(self.points) ==1:
            return
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
            red[i][j] = 255
            green[i][j] = blue[i][j] = 0


    def find_fv(self):
        heigth= self.boundingbox[3]/2
        LFT= []
        RGT= []

        for point in self.boundary:
            if point[1]> heigth:
                RGT.append(point)
            else: LFT.append(point)


        #key direction, value indx
        #up, down , left, right ,t-left,t-right, bot-l, bot-r

        keys = {(-1, 0): 0, (1, 0): 1, (0, -1): 2, (0, 1): 3,
                (-1, -1): 4, (-1, 1): 5, (1, -1): 6, (1, 1): 7}

        # feature vector
        FV = np.zeros(16)
        for x in ( LFT, RGT):
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
        sum = 0
        for i in range(len(FV)):
            sum += FV[i] * FV[i]
        magnitude = math.sqrt(sum)
        self.feature_vector = np.true_divide(FV, magnitude)

    def find_new_fv(self):

        dict= {(0,0,0,0): 0,(0,0,0,1): 1, (0,0,1,0): 2, (0,0,1,1):3,
               (0,1,0,0): 4, (0,1,0,1):5, (0,1,1,0):6, (0,1,1,1): 7,
               (1,0,0,0): 8, (1,0,0,1): 9, (1,0,1,0): 10, (1,0,1,1):11,
                (1,1,0,0): 12, (1,1,0,1): 13, (1,1,1,0): 14, (1,1,1,1): 15
               }

        backround= []
        FV = np.zeros(16)
        i_0 = self.boundingbox[1]
        j_0 = self.boundingbox[0]
        w = self.boundingbox[2]
        h = self.boundingbox[3]
        for row in range(i_0, i_0 - h, -1):
            for col in range(j_0, j_0 + w):
                if (row,col) not in self.points:
                    backround.append((row,col))


        for p in backround:
            dir= self.vector(p)
            indx= dict[dir]
            FV[indx]+=1
        sum = 0
        for i in range(len(FV)):
            sum += FV[i] * FV[i]
        magnitude = math.sqrt(sum)
        self.feature_vector = np.true_divide(FV, magnitude)

    def vector(self,p):
        dir=[0,0,0,0]
        #north
        qn= p
        while self.in_range((qn[0]-1,qn[1]), self.image):
            if qn in self.boundary:
                dir[0]=1
                break
            qn= (qn[0]-1, qn[1])

        #south
        qs= p
        while self.in_range((qs[0]+1,qs[1]), self.image):
            if qs in self.boundary:
                dir[1]=1
                break
            qs= (qs[0]+1, qs[1])
        #west

        qw = p
        while self.in_range((qw[0], qw[1]-1), self.image):
            if qw in self.boundary:
                dir[2] = 1
                break
            qw= (qw[0],qw[1] - 1)

        #east
        qe = p
        while self.in_range((qe[0], qe[1] + 1), self.image):
                if qe in self.boundary:
                    dir[3] = 1
                    break
                qe= (qe[0], qe[1] +1)

        return tuple(dir)





