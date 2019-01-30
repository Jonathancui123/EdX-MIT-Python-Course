print ('Please think of a integer between 0 and 100! (inclusive)')

low = 0
high = 100
guess = round((high + low)/2)


while True:
    print('Is', str(guess), 'your number?')
    user = input("enter 'h' if too high, 'l' if too low, or 'c' if correct!")
    if user == 'h':
        high = guess
    elif user == 'l':
        low = guess
    elif user == 'c':
        print ('Game over! Your number was:', str(guess))
        break
    else:
        print('Invalid input. Please input again.')
    guess = round((high + low) / 2)
    if high == low:
        print ('An error has occurred, please start again.')
        break





