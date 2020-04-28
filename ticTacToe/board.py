class Board:

    def __init__(self):
        self.board = [['-'] * 3 for y in range(0, 3)]

    def print_board(self):
        print('  (a)(b)(c)')
        for line in range(0, len(self.board)):
            print('({})'.format(line), end=' ')
            print(*self.board[line])

    def has_won(self, player):
        #vertical and horizontal
        for x in range(0, 3):
            if (self.board[x][0] == self.board[x][1] == self.board[x][2] is not '-') or (self.board[0][x] == self.board[1][x] == self.board[2][x] is not  '-'):
                return True
        # diagonal
        if (self.board[1][1] == self.board[0][0] == self.board[2][2] is not '-') or (self.board[1][1] == self.board[2][0] == self.board[0][2] is not '-'):
            return True
        else:
            return False

    def is_possible_move(self, x, y):
        if x < 0 or x > 2 or y < 0 or y > 2 or self.board[y][x] != '-':
            return False
        else:
            return True

    def move(self, x, y, player):
        if self.is_possible_move(x, y):
            self.board[y][x] = player.get_symbol()
        else:
            raise Exception('Not a possible input.')

    def get_board(self):
        return self.board
