import pygame, cv2
class Image():

    def __init__(self, path_without_extension: object, extension: object) -> object:
        self.path = path_without_extension
        self.extension = extension
        self.image = pygame.image.load(self.path + self.extension)

        #self.rect=self.image.get_rect()

    def resize(self, height, width):
        image = cv2.imread(self.path + self.extension)
        cv2.imwrite(self.path + "_r" + self.extension, cv2.resize(image, (height, width)))
        assert isinstance(self.extension, object)
        self.image = pygame.image.load(self.path + "_r" + self.extension)