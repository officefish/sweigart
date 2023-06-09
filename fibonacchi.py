import sys
from argparse import ArgumentParser 

def exit():
    print('Thanks for playng!')
    sys.exit()

def userInput(): 
   
    while True:
        print('Ebter the Nth Fibonacci number you wish to')
        print('calculate (such as 5, 50, 1000, 9999), or QUIT to quit:')
        response = input('> ').upper()

        if response == 'QUIT':
            exit()

        if response.isdecimal() and int(response) !=0:
            nth = int(response)
            return nth

        print('Please enter a number greater than 0, or Quit.')


def fibonacchi(nth, outputFile):
    secondToLastNumber = 0
    lastNumber = 1
    fibNumbersCalculated = 2

    resulttr = ''
    
    while True:
        nextNumber = secondToLastNumber + lastNumber
        fibNumbersCalculated += 1

        resulttr += nextNumber, ' '
        
        if fibNumbersCalculated == nth:
            print('The #', fibNumbersCalculated, ' Fibonacci ',
                  'number is ', nextNumber, sep='')
            break

        print(', ', end='')
        secondToLastNumber = lastNumber
        lastNumber = nextNumber

    if outputFile:
        pass
        resulttr
    else:
        pass
        #print to comsole

def printIntro():
    print('''Fibonacci Sequence, by Al Sweigart al@inventwithpyton.com
    The Fibonacci sequenc begins with 0 and 1, and the next number is the 
    sum of the previous two numbers. The sequens continues forever:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987...''')


def main():

    parser = ArgumentParser()
    parser.add_argument("-n", "--number", type = int, help='fibonacchi number limit')
    parser.add_argument('-o', '--output', type= str, help='output file')
    parser.add_argument('-b', '--benchmark', type= bool, help='calculate program datetime in milliseconds')

    args = parser.parse_args()
    nth = -1

    outputFile = None

    if args.number:
        nth = args.number

    if args.output:
        outputFile = args.output

    print('o: {}'.format(outputFile))
    
    
    #print('args: {}'.format(args))
    #pass
   #return

    printIntro()

    once = False
    outputFile = False
    benchmark = False

    # parseArguments
    
    while True:
        
        print()

        if nth < 0:
            nth = userInput()
        else:
            once = True      
        
        if nth == 1:
            print('0')
            print()
            print('The #1 Fibonacci number is 0.')
            continue
        elif nth == 2:
            print('0, 1')
            print()
            print('The #2 Fibonacci number is 1.')
            continue

        if nth >= 1000:
            print('WARNING: This will take a while to display on the')
            print(' screen. If you want to quit this program before it is')
            print('done, press, Ctrl-C')
            input('Press Enter to begin...')

       
        print('0, 1, ', end='')

        
        # startTime = date now() 
        fibonacchi(nth, outputFile)
        # endTime = date now()
        # total = endTime - startTime
        if benchmark:
            if outputFile: 
                pass # написать время в файл
            else:
                # print(buety total)
                pass 

        if once:
            exit()
            
    

main()




    

