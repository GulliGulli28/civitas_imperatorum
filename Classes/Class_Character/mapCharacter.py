from Classes.Class_Character.Character import Character
from Classes.Class_Character.Resident import Resident
from Classes.Class_Character.Walker import Walker
from Classes.Class_Character.Worker import Worker


class mapCharacter:
    _instance = None

    def __new__(cls):
        if mapCharacter._instance is None:
            mapCharacter._instance = super().__new__(cls)
        return mapCharacter._instance

    def __init__(self):
        self.list = []

    def add_character(self, character):
        self.list.append(character)

    def remove_character(self, character):
        self.list.remove(character)
