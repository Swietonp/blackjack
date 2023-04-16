from random import choice

from Player import Player


class Croupier(Player):
    def __init__(self, deck, player):
        super().__init__()
        self.deck = deck
        self.player = player
        self.user_choice = None
        self.game = True

    def play(self):
        self.deal_first_cards()
        self.deal_with_user_choice()

    def deal_first_cards(self):
        for _ in range(2):
            card_for_player = choice(self.deck)
            self.player.add_card(card_for_player)
            self.deck.delete_card(card_for_player)
            card_for_croupier = choice(self.deck)
            self.cards.append(card_for_croupier)
            self.deck.delete_card(card_for_croupier)
        self.print_partially_hide_state()
        self.player.print_current_state()

    def deal_with_user_choice(self):
        if self.player.total_value == 21:
            self.print_dashed_line()
            self.print_current_state()
            self.player.print_current_state()
            print('You have a BLACKJACK! You won!')
        else:
            self.get_user_choice()
            while self.game:
                if self.user_choice == 's':
                    self.print_dashed_line()
                    self.set_total_value_of_cards()
                    self.get_cards_for_croupier()
                    self.print_current_state()
                    self.player.print_current_state()
                    self.game = False
                    self.verify_state()
                elif self.user_choice == 'h':
                    self.print_dashed_line()
                    self.get_card_for_player()
                    if self.player.total_value == 21:
                        self.get_cards_for_croupier()
                        if self.total == 21:
                            self.print_current_state()
                            self.player.print_current_state()
                            print('DRAW!')
                            self.game = False
                        else:
                            self.print_current_state()
                            self.player.print_current_state()
                            print('YOU WON!')
                            self.game = False
                    elif self.player.total_value < 21:
                        self.print_partially_hide_state()
                        self.player.print_current_state()
                        self.user_choice = None
                        self.get_user_choice()
                    else:
                        self.print_current_state()
                        self.player.print_current_state()
                        print('YOU LOST!')
                        self.game = False
        self.print_dashed_line()

    def verify_state(self):
        if self.total > 21:
            print('YOU WIN!')
        elif self.total == self.player.total_value:
            print('DRAW!')
        elif self.total > self.player.total_value:
            print('YOU LOST!')
        elif self.total < self.player.total_value:
            print('YOU WIN!')

    def get_cards_for_croupier(self):
        self.set_total_value_of_cards()
        while self.total < 17:
            card_for_croupier = choice(self.deck)
            self.deck.delete_card(card_for_croupier)
            self.cards.append(card_for_croupier)
            self.set_total_value_of_cards()

    def get_card_for_player(self):
        card_for_player = choice(self.deck)
        self.deck.delete_card(card_for_player)
        self.player.cards.append(card_for_player)
        self.player.set_total_value_of_cards()

    def print_current_state(self):
        if self.cards:
            print('Croupier:', end=' ')
            for card in self.cards:
                print(card.rank, card.suit, end='  ')
            self.set_total_value_of_cards()
            print(f'Total: {self.total}')

    def get_user_choice(self):
        while not self.user_choice:
            self.user_choice = input('Do you want to [H]it or [S]tand ? : ').lower()
            if self.user_choice not in ['h', 's']:
                print('Incorrect input! Choose again.')
                self.user_choice = None

    def print_partially_hide_state(self):
        print('Croupier:', end=' ')
        print(self.cards[0].rank, self.cards[0].suit)

    @staticmethod
    def print_dashed_line():
        print('-'*50)
