import random

from .player import Player
from .board import Board

class Bot(Player):

    def __init__(self, symbol, name, board):
        Player.__init__(self, symbol, name, board)

    def enter_move(self):
        print(self.select_random_move())
        self.board.move(*self.select_random_move(), self)

    def select_random_move(self):
        unoccupied = []
        for y in range(0, 3):
            for x in range(0, 3):
                if self.board.is_possible_move(x, y):
                    unoccupied.append([x, y])
        random_entry = random.randint(0, len(unoccupied) - 1)
        return unoccupied[random_entry][0], unoccupied[random_entry][1]