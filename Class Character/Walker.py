import Character


class Walker(Character):
    reach = None
    distanceToBuilding = None
    travelHistory = None
    job = None

    def __init__(self, reach, distanceToBuilding, travelHistory, job):
        self.range = reach
        self.distanceToBuilding = distanceToBuilding
        self.travelHistory = travelHistory
        self.job = job
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

    