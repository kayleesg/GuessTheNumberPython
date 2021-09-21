#This is a guess the number game for Python3
import random

print('\nWelcome to Guess the Number\nA Simple Python3 Game made by:\nKaylee SG\nSee more stuff she\'s made on her github or visit her blog at\nkayleesg.github.io/kayleesgblog\n\n')
pName = input('Let\'s begin! What is your name?\n')    #Player's Name

guessesTaken = 0
number = random.randint(1, 20)

print('\n'+ pName + ', I am thinking of a number between 1 and 20.\nYou have 6 tries to guess it right!!\n')

# range of 6 so the game doesn't go on forever. After 6 tries, the for loop will break.
for guessesTaken in range(6):
    guess = int(input('Take a guess:\n'))

    if guess < 1 or guess > 20:
        print('You just wasted a try on a value that is out of scope. Try something between 1 and 20.')

    if guess < number:
        print('Your guess is too low.\n')
    elif guess > number:
        print('Your guess is too high.\n')
    else:
        break

#Code below reinforces the reason for the break of the for loop.
#If user broke the for loop because the guessed right, they'd get this message:
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + pName + '! You guessed my number in ' + guessesTaken + ' guesses!\n')

#If user broke the for loop because they reached the max number of guesses, they'd get this message:
if guess != number:
    number = str(number)
    print('Max guesses reached. The number I was thinking of was ' + number + '.\n')
