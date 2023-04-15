import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ["\u2663", "\u2665", "\u2666", "\u2660"]

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                                        for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def delete_card(self, card):
        self._cards.remove(card)


def get_blackjack_value(card):
    if isinstance(card, Card):
        if card.rank == 'J' or card.rank == 'Q' or card.rank == 'K':
            return 10
        if card.rank == 'A':
            return 11
        else:
            return int(card.rank)
    else:
        raise AttributeError('Given object is not a Card!')
