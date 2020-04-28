from hangman.drawHangman import draw_hangman

def play():
    answer = 'seal'
    decoded = ['_'] * len(answer)
    lost = False
    mistakes = 0
    print('Welcome to a game of hangman!\n\
    Can you solve this riddle before hangman is completly drawn?')
    print(*decoded, sep='  ')
    while not ''.join(decoded) == answer and not lost:
        guess = input('Guess a letter: ')[0].lower()
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    decoded[i] = guess
            print('Yayy that was right!')            
        else:
            print('That was wrong :(')
            mistakes += 1
            if mistakes == 6:
                lost = True
        draw_hangman(mistakes)
        print(*decoded, sep='  ')
    if lost:
        print('You lost')
    else:
        print('Wow you won')
    
