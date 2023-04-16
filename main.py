from FrenchDeck import FrenchDeck
from Player import Player
from Croupier import Croupier


def main():
    play = True
    while play:
        deck = FrenchDeck()
        player = Player()
        croupier = Croupier(deck, player)
        croupier.play()
        while True:
            choice = input('Do you want to play one more time? [Y/N] ').lower()
            if choice not in ['y', 'n']:
                print('Incorrect input!')
            else:
                if choice == 'n':
                    play = False
                    break
                elif choice == 'y':
                    break


if __name__ == '__main__':
    main()
