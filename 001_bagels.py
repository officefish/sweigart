
import random 

NUM_DIGITS = 3
MAX_GUESSES = 10

def getSecretNum(numDigits):
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(numDigits):
        secretNum += numbers.pop()
    return secretNum

def getClues(guess, secretNum):
    '''  '''
    if guess == secretNum:
        return 'You got it!'
    
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    
    if not len(clues):
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

def main():
    print("""Bages, a deductive logic game,
By Al Sweigart
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:     That means:
    Pico            One digit is correct but in the wrong position
    Fermi           One digit is correct but in the right position
    Bagels          No digit is correct

For example, if the secret number was 248 and your guess was 843, the 
clues would be Fermi Pico.""".format(NUM_DIGITS))

    while True:
        secretNum = getSecretNum(NUM_DIGITS)
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You run out of guesses.')
                print('The answer was {}.'.format(secretNum))

        print('Do you want to play again? (yes or now)')
        if not input('> ').lower().startswith('y'):
            break 
    print('Thanks for playing!')
    print(globals())

#if __name__ == '__main__':
main()

  
