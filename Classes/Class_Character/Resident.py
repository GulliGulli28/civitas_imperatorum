import Character


class Resident(Character):
    


    def liste_sprite_resident(self):
        if self.direction == NW:
            self.sprite_list= liste_sprites_NW_resident
        elif self.direction == NE:
            self.sprite_list= liste_sprites_NE_resident
        elif self.direction == SW:
            self.sprite_list= liste_sprites_SW_resident
        elif self.direction == SE:
            self.sprite_list= liste_sprites_SE_resident
