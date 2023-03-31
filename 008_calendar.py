""" """

import datetime
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',  'Nov', 'Dec')


def getCalendarFor(year, month):
    calText = ''
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
    calText += '... Sanday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'
    
    weekSeparator = ('+----------' * 7) + '+\n'
    blankRow = ('|          ' * 7) + '|\n'
    
    currentDate = datetime.date(year, month, 1)
    
    while currentDate.weekday() != 6:
        print(currentDate.weekday())
        currentDate -= datetime.timedelta(days=1)

    while True:
        calText += weekSeparator
            
        dayNumberRow = ''
        for i in range(7):
            day = str(currentDate.day)
            # print(day)
            dayNumberLabel = day.rjust(2)
            # print(dayNumberLabel)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)
    
        dayNumberRow += '|\n'
        calText += dayNumberRow
        for i in range(3):
            calText += blankRow

        if currentDate.month != month:
            break
    calText += weekSeparator
    return calText

# getCalendarFor(2022, 7)             

def main():
        
    print ('Calendar maker by Al Sweigart.')

    while True:
        print('Enter the year for the calendar:')
        response = input('> ')

        if response.isdecimal() and int(response) > 0:
            year = int(response)
            break

        print('Please enter a numerical year, like 2023')

    while True:
        print('Enter the month for the calendar, 1-12:')
        response = input('> ')

        if not response.isdecimal():
            print('Please enter anumeric month, like 3 for March')
            break

        month = int(response)
        if 1 <= month <= 12:
            break 

        print('Please enter a number fro 1 to 12.')


    calText = getCalendarFor(year, month)
    print(calText)

    calendarFileName = 'calendar_{}_{}.txt'.format(year, month)
    with open(calendarFileName, 'w') as fileObj:
        fileObj.write(calText)

    print('Saved to' + calendarFileName)

main()
