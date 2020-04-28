# from ticTacToe import main as play_ttt
import os

possible_games = {
    'Tic Tac Toe': 'tic_tac_toe.py',
    'Hangman': 'hangman/main.py'
}
print(f'Welcome to the Arcade.\n\
    What would you like to play?')
for possible_game, filename in possible_games.items():
    play = input(f'{possible_game} ? (y/n)')
    if play.lower() == 'y':
        with open(filename, "rb") as source_file:
            code = compile(source_file.read(), filename, "exec")
        exec(code)
