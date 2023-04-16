from FrenchDeck import get_blackjack_value


class Player:

    def __init__(self):
        self.cards = []
        self.total = None

    @property
    def total_value(self):
        if self.total:
            return self.total
        else:
            return 0

    def add_card(self, card):
        self.cards.append(card)

    def set_total_value_of_cards(self):
        self.total = sum(map(get_blackjack_value, self.cards))
        if self.total > 21 and 'A' in [card.rank for card in self.cards]:
            self.total -= 10

    def print_current_state(self):
        if self.cards:
            print('You have:', end=' ')
            for card in self.cards:
                print(card.rank, card.suit, end='  ')
            self.set_total_value_of_cards()
            print(f'Total: {self.total}')
