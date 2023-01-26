from Classes.Class_Character.Character import Character
from Classes.Class_Character.Resident import Resident
from Classes.Class_Character.Walker import Walker
from Classes.Class_Character.Worker import Worker


class mapCharacter:

    def __init__(self):
        self.list = []

    def add_character(self, character):
        self.list.append(character)

    def remove_character(self, character):
        self.list.remove(character)
