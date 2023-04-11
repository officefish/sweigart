import sys, time
import sevseg 

st = 30

def run(secondsLeft):
    """ Function that runs timer """
    try:
        while True:
            print('\n' * 60)
            hours = str(secondsLeft // 3600)
            minutes = str((secondsLeft % 3600) // 60)
            seconds = str(secondsLeft % 60)
            hDigits = sevseg.getSevSegStr(hours, 2)
            hTopRow, hMiddelRow, hBottomRow = hDigits.splitlines()

            mDigits = sevseg.getSevSegStr(minutes, 2)
            mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

            sDigits = sevseg.getSevSegStr(seconds, 2)
            sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

            print(hTopRow    + '     ' + mTopRow    + '     ' + sTopRow)
            print(hMiddelRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
            print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)

            if secondsLeft == 0:
                print()
                print('    * * * * BOOM * * * *')
                break
            print()
            print('Press Ctrl-C to quit.')

            time.sleep(1)
            secondsLeft -= 1
    except KeyboardInterrupt:
        print('Countdown, by Al Sweigart al@inventwithpython.com')
        sys.exit()

def __main__():
    
    args = sys.argv
    st = int(args[1])
    #print(args)
    run(st)

__main__()