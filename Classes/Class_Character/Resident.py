from Classes.Class_Character.Character import Character


class Resident(Character):

    def __init__(self, health, joy, positionX, positionY, direction, sprite_list, sprite_in_list):
        super().__init__(health, joy, positionX, positionY, direction, sprite_list, sprite_in_list)
    


    def liste_sprite_resident(self):
        if self.direction == NW:
            self.sprite_list= liste_sprites_NW_resident
        elif self.direction == NE:
            self.sprite_list= liste_sprites_NE_resident
        elif self.direction == SW:
            self.sprite_list= liste_sprites_SW_resident
        elif self.direction == SE:
            self.sprite_list= liste_sprites_SE_resident
