from Classes.Class_Character.Character import Character


class Migrant(Character):

    def __init__(self, positionX, positionY, dest):
        super().__init__(positionX, positionY, (0, 1))
        self.name = "migrant"
        self.dest = dest
        self.is_there = False

    def update(self):
        if not self.is_there:
            self.move

    def move(self):
        (x, y) = self.dest
        if x != self.positionX:
            self.positionX += 1
        if y < self.positionY:
            self.positionY -= 1
        elif y > self.positionY:
            self.positionY += 1
        else:
            self.is_there = True
