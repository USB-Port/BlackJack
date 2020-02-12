import pygame


class Card:
    image = pygame.image.load('img/cards.png')
    image = pygame.transform.scale(image, (1275, 700))

    def __init__(self, x, y, x2, y2):
        super().__init__()

        self.image.convert()
        self.image.set_alpha(128)
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.blit = (x, y, x2-x, y2-y)

    def draw(self, screen):
        screen.blit(self.image, self.rect, self.blit)

    def draw_at(self, screen, x, y):
        screen.blit(self.image, (x, y), self.blit)

    def set_rect(self, x, y):
        self.rect = (x, y)
