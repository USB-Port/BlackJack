

class Dealer:
    hand = 0

    def __init__(self):
        pass

    @property
    def get_hand(self):
        return self.hand

    def set_hand(self, value):
        self.hand = value
