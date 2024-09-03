color = 'blue'
guess = ''
guesses = 0

while (guess != color):
    guess = input('Em que cor está pensando?')
    guesses = guesses + 1
    if guess == color:
        print('you got it! it took you ', guesses, 'guess')
    elif guess == color and guesses > 1:
        print('you got it! it took you ', guesses, 'guesses')
