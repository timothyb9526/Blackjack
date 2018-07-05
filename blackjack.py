from random import randint, shuffle


def blackjack():
    deck = [
        2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
        10, 10, 10, 10, 11, 11, 11, 11
    ]
    shuffle(deck)
    blackjack_hand = []
    dealer_hand = []
    count = 0

    for _ in range(2):
        blackjack_hand.append(deck.pop())
        dealer_hand.append(deck.pop())

    while sum(blackjack_hand) < 22:
        count += 1
        print('{} player: {}, dealer: {}'.format(count, sum(blackjack_hand),
                                                 dealer_hand[0]))
        if sum(blackjack_hand) == 21:
            break
        option = input('Would you like to hit or stay? enter "h" to hit. ')
        if option == 'h':
            blackjack_hand.append(deck.pop())
            continue
        else:
            break

    while sum(blackjack_hand) < 22 and sum(dealer_hand) < 22:
        if sum(dealer_hand) < 17:
            dealer_hand.append(deck.pop())
            print('dealer hits!')
            input('press any key to continue')
        elif sum(dealer_hand) >= 17:
            print('dealer stays')
            break

    print('{} player: {}, dealer: {}'.format(count, sum(blackjack_hand),
                                             sum(dealer_hand)))

    if sum(blackjack_hand) > 21 and sum(dealer_hand) <= 21:
        print('DEALER WINS')
    elif sum(dealer_hand) > 21 and sum(blackjack_hand) <= 21:
        print('YOU WIN')
    elif sum(dealer_hand) > 21 and sum(blackjack_hand) > 21:
        print('BUST')
    elif sum(dealer_hand) == sum(blackjack_hand):
        print('PUSH')
    elif (sum(blackjack_hand) > sum(dealer_hand)):
        print('YOU WIN')
    elif sum(blackjack_hand) < sum(dealer_hand):
        print('DEALER WINS')


def main():
    blackjack()


if __name__ == '__main__':
    main()
