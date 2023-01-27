from Classes.Class_Character.Character import Character


class Walker(Character):
    reach = None
    distanceToBuilding = None
    travelHistory = None
    job = None
    mainBuilding = None

    def __init__(self, positionX, positionY, reach, distanceToBuilding, travelHistory, job, mainBuilding):
        super.__init__(positionX, positionY)
        self.range = reach
        self.distanceToBuilding = distanceToBuilding
        self.travelHistory = travelHistory
        self.job = job
        self.outOfRange = False
        self.mainBuilding = mainBuilding

    def move(self, build_map):
        if self.outOfRange:  # if the character is too far from his main building, he need to go back to him
            (x, y) = self.travelHistory[len(self.travelHistory)]
            super().positionX = x
            super().positionY = y
            if len(self.travelHistory) == 0:  # if the character is returned to his main building outOfRange=false
                self.outOfRange = False
        else:
            super().move(build_map)
            if (self.positionX, self.positionY) in self.travelHistory:  # if the character has already passed through
                # this position then we reduce the travelHistory from iteration 0 to the iteration in which he has
                # already passed
                del self.travelHistory[
                    self.travelHistory.index((self.positionX, self.positionY)):len(self.travelHistory)]
            else:  # else we add the position to the travelHistory
                self.travelHistory.append((self.positionX, self.positionY))  # add the position to the travelHistory
            if self.mainBuilding.getRange() < self.distanceToBuilding:  # If the character is too far from his main
                # building
                self.outOfRange = True
        self.updateDistanceToBuilding()

    def updateDistanceToBuilding(self):
        """
        Update the distance between the character and his main building
        :return:
        """
        build_pos_x = self.mainBuilding.getPositionX()  # get the Building posX
        build_pos_y = self.mainBuilding.getPositionY()  # get the Building posY
        max_distance = abs(build_pos_x - self.positionX)  # maximum distance calculation
        if abs(build_pos_y - self.positionY) > max_distance:
            max_distance = abs(build_pos_y - self.positionY)
        self.distanceToBuilding = max_distance  # assign the new distance


""" POUR ANIMATION
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
