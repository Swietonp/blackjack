from FrenchDeck import FrenchDeck
from Player import Player
from Croupier import Croupier


def main():
    is_game_live = True
    while is_game_live:
        deck = FrenchDeck()
        player = Player()
        croupier = Croupier(deck, player)
        croupier.play()
        choice = input('Do you want to play one more time? [Y/N] ').lower()
        if choice not in ['y', 'n']:
            print('Incorrect input!')
        else:
            if choice == 'n':
                is_game_live = False


if __name__ == '__main__':
    main()
