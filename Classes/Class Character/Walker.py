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

    def liste_sprite_walker(self):
        if self.direction == NW:
            self.sprite_list == liste_sprites_NW_walker
        elif self.direction == NE:
            self.sprite_list == liste_sprites_NE_walker
        elif self.direction == SW:
            self.sprite_list == liste_sprites_SW_walker
        elif self.direction == SE:
            self.sprite_list == liste_sprites_SE_walker

    def move (self,"""map.getPossibleDirection(self.positionX,self.positionY)"""): #avec la modif du todo de Character.move()
        if self.outOfRange:#if the character is too far from his main building, he need to go back to him
            self.move(self,self.travelHistory[len(self.travelHistory)])
            if len(self.travelHistory) != 0:#if the character is returned to his main building outOfRange=false
                self.outOfRange = False
        self.move(self,"""map.getPossibleDirection(self.positionX,self.positionY)""")
        if self.mainBuilding.getRange()<self.distanceToBuilding:#If the character is too far from his main building
            self.outOfRange = True
        self.updateDistanceToBuilding(self)

    def updateDistanceToBuilding(self):
        BposX = self.mainBuilding.getPositionX()#get the Building posX
        BposY = self.mainBuilding.getPositionY()#get the Building posY
        maxDistance = abs(BposX-self.positionX)#maximum distance calculation
        if abs(BposY-self.positionY)>maxDistance:
            maxDistance = abs(BposY-self.positionY)
        self.distanceToBuilding=maxDistance#assign the new distance