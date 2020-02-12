from classes.Card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(0, 4):
            for k in range(0, 13):
                self.cards.append(Card((k*98), (i * 175), (k*97) + 105, (i * 175) + 175))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, screen):
        self.cards[0].draw_at(screen, 400, 0)
        self.cards[1].draw_at(screen, 510, 0)

        self.cards[2].draw_at(screen, 400, 500)
        self.cards[3].draw_at(screen, 510, 500)
