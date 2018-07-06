from random import randint, shuffle


def card_score(card):
    if isinstance(card, int):
        return card
    elif card == 'J':
        card = 10
    elif card == 'K':
        card = 10
    elif card == 'Q':
        card = 10
    elif card == 'A':
        card = 11
    return card


def hand_score(hand):
    total = 0
    for card in hand:
        total += card_score(card)
    return total


def hand_scores(hand):
    '''
    >>> hand_scores([2,3,4])
    [9]
    >>> hand_scores(['Q', 2, 5])
    [17]
    >>> hand_scores(['A', 5])
    [6, 16]
    >>> hand_scores(['A', 5, 'A'])
    [7, 17, 27]
    '''
    interpretations = []
    hand_card_scores = []

    if not hand:
        return [[]]
    elif hand[0] == 'A':
        sub_interps = interpretations(hand[1:])
        as_one = [[1] + sub for sub in sub_interps]
        as_eleven = [[11] + sub for sub in sub_interps]
        return as_one + as_eleven
    else:
        sub_interps = interpretations(hand[1:])
        as_self = [card_score[hand[0]] + sub for sub in sub_interps]
        return as_self


def blackjack():

    deck = [
        2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'Q', 'Q', 'Q', 'Q', 'K', 'K',
        'K', 'K', 'J', 'J', 'J', 'J', 'A', 'A', 'A', 'A'
    ]

    shuffle(deck)
    blackjack_hand = []
    dealer_hand = []
    for _ in range(2):
        blackjack_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
    while hand_score(blackjack_hand) < 22:

        print('player: {}, dealer: {}'.format(
            hand_score(blackjack_hand), dealer_hand[0]))
        if hand_score(blackjack_hand) == 21:
            break
        option = input('Would you like to hit or stay? enter "h" to hit. ')
        if option == 'h':
            blackjack_hand.append(deck.pop())
            continue
        else:
            break
    print(blackjack_hand, dealer_hand[0])

    while hand_score(blackjack_hand) < 22 and hand_score(dealer_hand) < 22:
        if hand_score(dealer_hand) <= 17:
            dealer_hand.append(deck.pop())
            print('dealer hits!')
            input('press any key to continue')
        elif hand_score(dealer_hand) >= 17:
            print('dealer stays')
            break

    print('player: {}, dealer: {}'.format(
        hand_score(blackjack_hand), hand_score(dealer_hand)))
    print(blackjack_hand, dealer_hand)

    if hand_score(blackjack_hand) > 21 and hand_score(dealer_hand) < 21:
        print('DEALER WINS')
    elif hand_score(dealer_hand) > 21 and hand_score(blackjack_hand) < 21:
        print('YOU WIN')
    elif hand_score(dealer_hand) > 21 and hand_score(blackjack_hand) > 21:
        print('BUST')
    elif hand_score(dealer_hand) == hand_score(blackjack_hand):
        print('PUSH')
    elif (hand_score(blackjack_hand) > hand_score(dealer_hand)):
        print('YOU WIN')
    elif hand_score(blackjack_hand) < hand_score(dealer_hand):
        print('DEALER WINS')


def main():
    blackjack()


if __name__ == '__main__':
    main()
