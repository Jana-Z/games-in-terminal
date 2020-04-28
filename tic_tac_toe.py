from ticTacToe.board import Board
from ticTacToe.bot import Bot
from ticTacToe.game import Game
from ticTacToe.player import Player

def main():
    board = Board()
    bot = Bot('x', 'bot', board)
    print(f'symbol: {bot.get_symbol()}')
    game = Game(None, None)
    game.start()

main()