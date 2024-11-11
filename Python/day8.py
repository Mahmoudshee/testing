trial = 3
starting = 1
guessing = 'kenty'

print('You have only 3 trials to guess the right word')

while starting <= trial:
    guess = input('Guess the word: ')
    if guess == 'kenty':
        print('You won!!')
        break
    else:
        print(f"try again ")
        starting += 1
if starting > trial:
    print(f'you trials are done you limit of trials reached {starting} ')

