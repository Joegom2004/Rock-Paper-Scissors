import random
RPS = ['rock', 'paper', 'scissors']
your_guess = input('Pick "R", "P" or "S": ')
your_guess = your_guess.upper()
while True:
    if your_guess == "R":
        your_guess = RPS[0]
        break
    elif your_guess == "P":
        your_guess = RPS[1]
        break
    elif your_guess == "S":
        your_guess = RPS[2]
        break
    else:
        print('Error, Try Again!')
        your_guess = input('Pick "R", "P" or "S": ')

my_guess = random.choice(('rock', 'paper', 'scissors'))

while True:
    if my_guess == your_guess:
        print(f'Player({your_guess}) : CPU({my_guess})')
        print(f'{your_guess} is equal to {my_guess}')
        your_guess = input('Pick "R", "P" or "S": ')
        your_guess = your_guess.upper()
        if your_guess == "R":
            your_guess = RPS[0]
        elif your_guess == "P":
            your_guess = RPS[1]
        elif your_guess == "S":
            your_guess = RPS[2]
        my_guess = random.choice(('rock', 'paper', 'scissors'))
    elif my_guess == 'rock' and your_guess == 'scissors':
        print(f'Player({your_guess}) : CPU({my_guess})')
        print ('CPU win, Rock!')
        break
    elif my_guess == 'rock' and your_guess == 'paper':
        print(f'Player({your_guess}) : CPU({my_guess})')
        print('Player win!, Paper!')
        break
    elif my_guess == 'scissors' and your_guess == 'paper':
        print(f'Player({your_guess}) : CPU({my_guess})')
        print('CPU win, Scissors!')
        break
    elif my_guess == 'scissors' and your_guess == 'rock':
        print(f'Player({your_guess}) : CPU({my_guess})')
        print('Player win, Rock!')
        break
    elif my_guess == 'paper' and your_guess == 'rock':
        print(f'Player({your_guess}) : CPU({my_guess})')
        print('CPU win, Paper!')
        break
    elif my_guess == 'paper' and your_guess == 'scissors':
        print(f'Player({your_guess}) : CPU({my_guess})')
        print('Player win, Scissors!')
        break
    else:
        print('Error, Try Again!')
        your_guess = input('Pick "R", "P" or "S": ')
        your_guess = your_guess.upper()
        if your_guess == "R":
            your_guess = RPS[0]
        elif your_guess == "P":
            your_guess = RPS[1]
        elif your_guess == "S":
            your_guess = RPS[2]
        my_guess = random.choice(('rock', 'paper', 'scissors'))
    