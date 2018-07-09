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
    elif card == 'Ace':
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


def get_num_players():
    while True:
        num_players = input('How many players? ').strip()
        if num_players.isdigit():
            int_num_players = int(num_players)
            if int_num_players > 0 and int_num_players <= 4:
                return int_num_players
        print('invalid num of players')


def blackjack():

    deck = [
        2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'Q', 'Q', 'Q', 'Q', 'K', 'K',
        'K', 'K', 'J', 'J', 'J', 'J', 'A', 'A', 'A', 'A'
    ]
    for _deck in range(6):
        for _suit in range(4):
            for i in range(2, 11):
                deck.append(i)
            for _facecard in range(3):
                deck.append(10)
                deck.append('Ace')
    shuffle(deck)

    num_players = get_num_players()

    players = []
    for i in range(num_players):
        player_name = 'Player {}'.format(i + 1)
        players.append({'name': player_name, 'cards': [], 'money': 100})
    for player in players:
        player['cards'].append(deck.pop())
        player['cards'].append(deck.pop())

    print(players)
    input()

    # player_1_hand = []
    # player_2_hand = []
    # player_3_hand = []
    # player_4_hand = []
    # dealer_hand = []
    # betting_amount = []
    # players = [player_1_hand, player_2_hand, player_3_hand, player_4_hand]
    # for _ in range(2):
    #     player_1_hand.append(deck.pop())
    #     player_2_hand.append(deck.pop())
    #     player_3_hand.append(deck.pop())
    #     player_4_hand.append(deck.pop())
    #     dealer_hand.append(deck.pop())

    # players_in_game = input('How many players will be playing today? ')
    # if int(players_in_game) > 4:
    #     print('We can only have four players at a time. ')
    #     return
    # else:
    #     print()

    # for name in players: # first way
    #     bet_amount = input('How much would you like to bet? ')
    #     betting_amount.append(int(bet_amount))
    #     print(betting_amount)

    # for player in players: # second way
    #     bet_amount = input('How much would you like to bet? ')
    #     player['money'] = input(bet_amount)

    while hand_score(player_1_hand) < 22:
        print('player1: {}, player2: {}, player3: {}, player4: {}, dealer: {}'.
              format(
                  hand_score(player_1_hand), hand_score(player_2_hand),
                  hand_score(player_3_hand), hand_score(player_4_hand),
                  dealer_hand[0]))
        if hand_score(player_1_hand) == 21:
            break
        option = input('Would you like to hit or stay? enter "h" to hit. ')
        print()
        if option == 'h':
            player_1_hand.append(deck.pop())
            continue
        else:
            break
    while hand_score(player_2_hand) < 22:

        print('player1: {}, player2: {}, player3: {}, player4: {}, dealer: {}'.
              format(
                  hand_score(player_1_hand), hand_score(player_2_hand),
                  hand_score(player_3_hand), hand_score(player_4_hand),
                  dealer_hand[0]))

        if hand_score(player_2_hand) == 21:
            break
        option = input('Would you like to hit or stay? enter "h" to hit. ')
        print()
        if option == 'h':
            player_2_hand.append(deck.pop())
            continue
        else:
            break
    while hand_score(player_3_hand) < 22:

        print('player1: {}, player2: {}, player3: {}, player4: {}, dealer: {}'.
              format(
                  hand_score(player_1_hand), hand_score(player_2_hand),
                  hand_score(player_3_hand), hand_score(player_4_hand),
                  dealer_hand[0]))

        if hand_score(player_3_hand) == 21:
            break
        option = input('Would you like to hit or stay? enter "h" to hit. ')
        print()
        if option == 'h':
            player_3_hand.append(deck.pop())
            continue
        else:
            break
    while hand_score(player_4_hand) < 22:

        print('player1: {}, player2: {}, player3: {}, player4: {}, dealer: {}'.
              format(
                  hand_score(player_1_hand), hand_score(player_2_hand),
                  hand_score(player_3_hand), hand_score(player_4_hand),
                  dealer_hand[0]))

        if hand_score(player_4_hand) == 21:
            break
        option = input('Would you like to hit or stay? enter "h" to hit. ')
        print()
        if option == 'h':
            player_4_hand.append(deck.pop())
            continue
        else:
            break

    print('player1: {}, player2: {}, player3: {}, player4: {}, dealer: {}'.
          format(player_1_hand, player_2_hand, player_3_hand, player_4_hand,
                 dealer_hand[0]))

    while hand_score(player_1_hand) < 22 or hand_score(
            player_2_hand) or hand_score(player_3_hand) or hand_score(
                player_4_hand) or hand_score(dealer_hand) < 22:
        if hand_score(dealer_hand) <= 17:
            dealer_hand.append(deck.pop())
            print('dealer hits!')
            print()
            input('press any key to continue')
            print()
        elif hand_score(dealer_hand) >= 17:
            print('dealer stays')
            print()
            break

    print('player1: {}, player2: {}, player3: {}, player4: {}, dealer: {}'.
          format(
              hand_score(player_1_hand), hand_score(player_2_hand),
              hand_score(player_3_hand), hand_score(player_4_hand),
              hand_score(dealer_hand)))
    print('player1: {}, player2: {}, player3: {}, player4: {}, dealer: {}'.
          format(player_1_hand, player_2_hand, player_3_hand, player_4_hand,
                 dealer_hand[0]))

    if hand_score(player_1_hand) > 21 and hand_score(dealer_hand) < 21:
        print('DEALER WINS')
        print('Dealer Wins: ${}'.format(sum(betting_amount)))
    elif hand_score(dealer_hand) > 21 and hand_score(player_1_hand) <= 21:
        print('PLAYER1 WINS')
        print('Player1 Wins: ${}'.format(sum(betting_amount)))
    elif hand_score(dealer_hand) > 21 and hand_score(player_1_hand) > 21:
        print('BUST')
    elif hand_score(dealer_hand) == hand_score(player_1_hand):
        print('PUSH')
    elif (hand_score(player_1_hand) > hand_score(dealer_hand)):
        print('PLAYER1 WINS')
        print('Player1 Wins: ${}'.format(sum(betting_amount)))
    elif hand_score(player_1_hand) < hand_score(dealer_hand):
        print('DEALER WINS')
        print('Dealer Wins: ${}'.format(sum(betting_amount)))
    elif hand_score(dealer_hand) > 21 and hand_score(player_2_hand) < 21:
        print('PLAYER2 WINS')
        print('Player2 Wins: ${}'.format(sum(betting_amount)))
    elif hand_score(dealer_hand) > 21 and hand_score(player_3_hand) < 21:
        print('PLAYER3 WINS')
        print('Player3 Wins: ${}'.format(sum(betting_amount)))
    elif hand_score(dealer_hand) > 21 and hand_score(player_4_hand) < 21:
        print('PLAYER4 WINS')
        print('Player4 Wins: ${}'.format(sum(betting_amount)))


def main():
    blackjack()


if __name__ == '__main__':
    main()
