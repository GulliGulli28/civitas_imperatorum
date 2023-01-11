import Character


class Walker(Character):
    reach = None
    distanceToBuilding = None
    travelHistory = None
    job = None
    mainBuilding = None

    def __init__(self, reach, distanceToBuilding, travelHistory, job, mainBuilding):
        self.range = reach
        self.distanceToBuilding = distanceToBuilding
        self.travelHistory = travelHistory
        self.job = job
        self.outOfRange = False
        self.mainBuilding = mainBuilding
        super().__init__()

"""
    def liste_sprite_walker(self):
        if self.direction == NW:
            self.sprite_list == liste_sprites_NW_walker
        elif self.direction == NE:
            self.sprite_list == liste_sprites_NE_walker
        elif self.direction == SW:
            self.sprite_list == liste_sprites_SW_walker
        elif self.direction == SE:
            self.sprite_list == liste_sprites_SE_walker
"""


    def move (self, build_map):
        if self.outOfRange:#if the character is too far from his main building, he need to go back to him
            (x, y)=self.travelHistory[len(self.travelHistory)]
            self.positionX=x
            self.positionY=y
            if len(self.travelHistory) == 0:#if the character is returned to his main building outOfRange=false
                self.outOfRange = False
        else:

            if (self.positionX, self.positionY) in self.travelHistory:#if the character has already passed through this position then we reduce the travelHistory from iteration 0 to the iteration in which he has already passed
                del self.travelHistory[self.travelHistory.index((self.positionX,self.positionY)):len(self.travelHistory)]
            else :#else we add the position to the travelHistory
                self.travelHistory.append((self.positionX,self.positionY))#add the position to the travelHistory
            if self.mainBuilding.getRange() < self.distanceToBuilding:  # If the character is too far from his main building
                self.outOfRange = True
        self.updateDistanceToBuilding(self)


    def updateDistanceToBuilding(self):
        BposX = self.mainBuilding.getPositionX()#get the Building posX
        BposY = self.mainBuilding.getPositionY()#get the Building posY
        maxDistance = abs(BposX-self.positionX)#maximum distance calculation
        if abs(BposY-self.positionY)>maxDistance:
            maxDistance = abs(BposY-self.positionY)
        self.distanceToBuilding=maxDistance#assign the new distance