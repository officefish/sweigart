"""
Black Jack. By Al Sweigart copyright...
"""

import random, sys

HEARTS = chr(9829) # ascii symbol of HEARTS
DIAMONDS = chr(9830) # ascii symbol of DIAMONDS
SPADES = chr(9824) # ascii symbol of SPADES
CLUBS = chr(9827) # ascii symbol of CLUBS

BACKSIDE = 'backside'

BLACK_JACK = 21
DEALER_LIMIT = 17

def getBet(maxBet):
    ''' Спрашивает у игрока сколько он ставит на этом раунде'''
    while True: # Продолжаем спрашивать, пока не будет введено допустимое значение
        print('How much do you want to bet? 1-{} or QUIT'.format(maxBet))
        bet = input('> '.upper().strip())
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        
        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

def getDeck():
    '''Возвращает список кортежей (номинал, масть) для всех 52 карт.'''
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    """ Отображает карты игрока и дилера. Скрывает первую карту 
    у дилера, если showDealerHand = False. """
    print()
    if showDealerHand:
        print('Dealer\'s hand:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('Dealer\'s hand: ???')
        # Скрываем первую карту у дилера
        displayCards([BACKSIDE] + dealerHand[1:])
    # Отображаем карты игрока
    print('Player\'s hand:', getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    """ """
    value = 0
    numberOfAces = 0

    for card in cards:
        #print(card[0], card[1])
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)
    
    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10
    
    return value

def displayCards(cards):
    ''' '''
    rows = ['', '', '', '', '']
    for i, card in enumerate(cards):
        rows[0] += ' ___  '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
   
    for row in rows:
        print(row)

def getMove(playerHand, money):
    '''  '''
    while True:
        moves = ['(H)it', '(S)tand']

        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
        
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D':
            return move

def main():
    print("""Welcome to Black Jack. By Al Sweigart.
    
    Rules: 
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards. 
        On your first play you can (D)ouble down to increase your bet
        but most hit exactly one more time before standing.
        In case of tie, the bet is returned ti the player.
        The dealer stop hitting at 17.""")

    money = 5000
    while True:
        if money <= 0:
            print("You're broke!")
            print('Good thing you weren\'t playing with real money.')
            print('Thanks for playing!')
            sys.exit()

        print('Money: ', money)
        bet = getBet(money)

        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        print('Bet: ', bet)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()

            if getHandValue(playerHand) > BLACK_JACK: 
                break

            move = getMove(playerHand, money - bet)

            if move == 'D':
                # 'Удваиваю': Игрок удваивает, он может увеличить ставку
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to {}'.format(bet))
                print('Bet: ', bet)

            if move in ('H', 'D'):
                # 'Еще' или 'Удваиваю': Игрок берет еще одну карту
                newCard = deck.pop()
                rank, suit = newCard
                print('Your drew a {} of {}'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > BLACK_JACK:
                    # У игрока перебор
                    continue

            if move in ('S', 'D'):
                # 'Хватит' или 'Удваиваю': Переход хода к другому игроку
                break

            # Обработка действий дилера:
            if getHandValue(playerHand) <= BLACK_JACK:
                while getHandValue(dealerHand) < DEALER_LIMIT:
                    print('Dealer hits...')
                    dealerHand.append(deck.pop)
                    displayHands(playerHand, dealerHand, False)

                    if getHandValue(dealerHand) > BLACK_JACK:
                        break # У дилера перебор
                    input('Press enter to continue...')
                    print('\n\n')

            # Отображает итоговые карты на руках.
            displayHands(playerHand, dealerHand, True)

            playerValue = getHandValue(playerHand)
            dealerValue = getHandValue(dealerHand)
            
            # Проверяем выиграл ли игрок.
            if dealerValue > BLACK_JACK:
                print('Dealer busts! You win ${}!'.format(bet))
                money += bet
            elif playerValue > BLACK_JACK:
                print('You lost!')
                money -= bet
            elif playerValue > dealerValue:
                print('You won ${}!'.format(bet))
            elif playerValue == dealerValue:
                print('It\'s a tie! The bet is returned to you.')
            
            input('Press enter to continue...')
            print('\n\n')

if __name__ == '__main__':
    main()






                    
                








