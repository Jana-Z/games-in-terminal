from .board import Board
from .player import Player
from .bot import Bot

class Game:

    def __init__(self, player1, player2):
        self.board = Board()
        if player1 == None and player2 == None:
            self.player1 = Player('x', self.board, 'Spieler')
            self.player2 = Bot('o', self.board, 'Botty McBot')
        else:
            self.player1 = player1
            self.player2 = player2
        self.winner = None

    def start(self):
        print('\n Welcome to a game of TicTacToe! \n')
        print('This is the playing board: ')
        self.board.print_board()
        curr_player = self.player1
        for turn in range(0, 10):
            print('\nIt is your turn {}'.format(curr_player.get_name()))
            curr_player.enter_move()
            self.board.print_board()
            if self.board.has_won(curr_player):
                self.winner = curr_player
                print("Congragulations {}! You have won!".format(curr_player.get_name()))
                break
            curr_player = self.player1 if curr_player == self.player2 else self.player2