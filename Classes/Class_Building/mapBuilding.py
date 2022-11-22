import Building

class mapBuilding():
    def __init__(self):
        self.sizeX = 50
        self.sizeY = 50
        self.map = [[None for j in range(self.sizeY)] for i in range(self.sizeX)]

    def add_build (self, newbuild):
        self.map[newbuild.positionX][newbuild.positionY] = Building
        if newbuild.size>1:
            for i in range(newbuild.size):
                i+=1
                p = Pointeur()
                for y in range(i):
                    self.map[newbuild.positionX+i][newbuild.positionY+y]=p
                    self.map[newbuild.positionX+y][newbuild.positionY+i]=p
                self.map[newbuild.positionX+i][newbuild.positionY+i] = p




