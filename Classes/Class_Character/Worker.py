from Classes.Class_Character.Character import Character


class Worker(Character):
    

    def liste_sprite_worker(self):
        if self.direction == NW:
            self.sprite_list= liste_sprites_NW_worker
        elif self.direction == NE:
            self.sprite_list= liste_sprites_NE_worker
        elif self.direction == SW:
            self.sprite_list= liste_sprites_SW_worker
        elif self.direction == SE:
            self.sprite_list= liste_sprites_SE_worker



