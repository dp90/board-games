from dataclasses import dataclass
from typing import List
from boardgames.interfaces import IPlayer, IGame


class Worms(IGame):
    def __init__(self, players: List[IPlayer]):
        super().__init__(players)
        self.current_player = self._select_first_player()
        self.remaining_chips = InitialChipSet().chips
        self.end_of_game = False

    def play(self):
        while not self.end_of_game:
            self.show_score()
            self.current_player.take_turn()
            self.end_of_game = self.check_end_of_game()
            self.next_player()
        self.declare_winner()
        self.show_score()

    def check_end_of_game(self):
        return not self.remaining_chips and self.current_player == self.players[-1]

    def show_score(self):
        for player in self.players:
            player.get_score()

    def declare_winner(self):
        # player(s) with max n_worms
        # Create list winners
        if len(winners) > 1:
            print(f"The winners are {*winners}!")
        else:
            print (f"The winner is {*winners}!")

    def next_player(self):
        self.current_player_id = self.current_player_id % len(self.players)

    def _validate_number_of_players(self):
        assert len(self.players) in range(2, 7), "Minimum number of players is 2 and maximum number is 6."

    def _select_first_player(self):
        return self.players[0]


class WormsPlayer(IPlayer):
    def __init__(self, id):
        super().__init__(id)
        self.chips = []
        self.n_worms = 0

    def take_turn(self):
        self.roll_dice(6)
        self.show_dice_roll()
        # ask what to keep
        # ask if roll dice
        
        self.ask_roll_dice()
        roll_dice = Input("")
        if roll_dice:
            dice_to_roll = Input("Give indices of dice to roll")
            self.validate_dice_availability()

    def roll_dice(self, n_dice):
        pass

    def select_dice(self, dice):
        pass

    def select_chip(self, chip):
        pass

    def get_score(self):
        print(f"Player {self.id}/n Latest chip: {self.chips[-1]}/n # Worms: {self.n_worms}")
    
    def show_dice_roll(self):
        pass

    def validate_dice_availability(self):
        pass


@dataclass
class WormsChip():
    dice_score: int
    worms: int


@dataclass
class InitialChipSet: 
    chips = (
    WormsChip(21, 1),
    WormsChip(22, 1),
    WormsChip(23, 1),
    WormsChip(24, 1),
    WormsChip(25, 1),
    WormsChip(26, 1),
    WormsChip(27, 1),
    WormsChip(28, 1),
    WormsChip(29, 1),
    WormsChip(30, 1),
    WormsChip(31, 1),
    WormsChip(32, 1),
    WormsChip(33, 1),
    WormsChip(34, 1),
    WormsChip(35, 1),
    WormsChip(36, 1),
)
