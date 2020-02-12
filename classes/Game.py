import sys
import pygame
from classes.Card import Card
from classes.Deck import Deck

class Game:
    image = pygame.image.load('img/dealer.png')

    def __init__(self):
        pygame.init()

        size = 1280, 720
        black = 0, 170, 0
        self.screen = pygame.display.set_mode(size)
        self.screen.fill(black)
        self.image.convert()
        self.image.set_alpha(128)
        self.rect = self.image.get_rect(topleft=(-200, 300))

        self.play()

    def play(self):
        card = Card(0, 0, 100, 175)
        deck = Deck()

        i = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_a:
                        pass

                    if event.key == pygame.K_s:
                        deck.shuffle()

                    if event.key == pygame.K_SPACE:
                        if i < 52:
                            i = i + 1


                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.image, self.rect)

            deck.deal(self.screen)


            pygame.display.flip()



