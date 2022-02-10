from abc import ABC, abstractmethod
from typing import List


class IPlayer(ABC):
    def __init__(self, id):
        self.id = id
    
    @abstractmethod
    def take_turn(self):
        raise NotImplementedError

    @abstractmethod
    def get_score(self):
        raise NotImplementedError


class IGame(ABC):
    def __init__(self, players: List[IPlayer]):
        self.players = players
        self._validate_number_of_players()
        self.current_player = self._select_first_player()

    @abstractmethod
    def play(self):
        raise NotImplementedError

    @abstractmethod
    def _validate_number_of_players(self):
        raise NotImplementedError

    @abstractmethod
    def _select_first_player(self):
        raise NotImplementedError
