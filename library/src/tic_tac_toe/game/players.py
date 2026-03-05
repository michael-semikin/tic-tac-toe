import random
import time
from abc import ABCMeta, abstractmethod

from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.minimax import find_best_move
from tic_tac_toe.logic.models import Mark, GameState, Move

class Player(metaclass=ABCMeta):
    def __init__(self, mark: Mark):
        self.mark = mark

    @abstractmethod
    def get_move(self, game_state: GameState) -> Move | None:
        """Return the current player's move in the given game state."""

    def make_move(self, game_state: GameState) -> GameState:
        if self.mark == game_state.current_mark:
            if move := self.get_move(game_state):
                return move.after_state
            raise InvalidMove("No more possible moves")
        else:
            raise InvalidMove("It's the other player's turn")


class ComputerPlayer(Player, metaclass=ABCMeta):
    def __init__(self, mark: Mark, delay_seconds: float = 0.25):
        super().__init__(mark)
        self.delay_seconds = delay_seconds

    @abstractmethod
    def get_computer_move(self, game_state: GameState) -> Move | None:
        """"""

    def get_move(self, game_state: GameState) -> Move | None:
        time.sleep(self.delay_seconds)
        return self.get_computer_move(game_state)


class RandomComputerPlayer(ComputerPlayer):
    def get_computer_move(self, game_state: GameState) -> Move | None:
        return game_state.make_random_move()


class MinimaxComputerPlayer(ComputerPlayer):
    def get_computer_move(self, game_state: GameState) -> Move | None:
        if game_state.game_not_started:
            return game_state.make_random_move()
        else:
            return find_best_move(game_state)