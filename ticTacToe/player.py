from .board import Board

class Player:

    def __init__(self, symbol, board, name=None):
        self.symbol = symbol
        self.name = name
        self.board = board
        if not name:
            self.name = input('Wie heißt du?')

    def enter_move(self):
        while True:
            print('\nIt is your turn Player {}\nWhich field would you like to take?\n'.format(self.symbol))
            # x = input('Please enter the x coordinate (a, b or c): ')
            # x = ord(x)%32 - 1
            # y = input('Please enter the y coordinate (0, 1 or 2): ')
            coordinates = input('Please enter the coordinate, f.ex. a1 / b2 / etc. ')
            x = ord(coordinates[0])%32 - 1
            y = coordinates[1]
            try:
                y = int(y)
            except:
                print('Not a correct input. Try again.')
            else:
                self.send_move(x, y)
                break

    def send_move(self, x, y):
        try:
            self.board.move(x, y, self)
        except Exception as e:
            print(e)

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name