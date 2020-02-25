from classes.Card import Card
import random


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(0, 4):
            for k in range(0, 13):
                card = Card((k * 98), (i * 175), (k * 97) + 105, (i * 175) + 175)
                card.value = k + 1
                if k > 10:
                    card.value = 10
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, screen, dealer, player):
        self.cards[0].draw_at(screen, 400, 0)
        self.cards[1].draw_at(screen, 510, 0)
        value = self.cards[0].value + self.cards[1].value
        dealer.set_hand(value)

        self.cards[2].draw_at(screen, 400, 500)
        self.cards[3].draw_at(screen, 510, 500)
        value = self.cards[2].value + self.cards[3].value
        player.set_hand(value)
