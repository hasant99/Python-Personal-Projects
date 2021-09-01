# This is a virtual version of the dice game "Pig".
# There can be up to 4 players who rotate taking turns.
# On each turn, the player must roll at least once.
# If player rolls a one, their turn ends.
# Any other number player rolls is added to their score.
# player can choose to keep rolling as long as they don't roll 1.
# If player rolls one at any point during their turn their score is set to 0.
# PLayers scores are only affected each round.

import random

def get_player_num():
    players = input('How many players are playing?\n')
    while (players.isnumeric() != True) or (int(players) < 1 or int(players) > 4):
        print('Please enter a valid number!')
        players = input('How many players are playing?')
    return int(players)


def main():
    num_of_players = get_player_num()
    player_scores = [0]*num_of_players
    temp_score = 0
    i = 1
    t = 1
    while True:
        roll = random.randint(1,6)
        print(player_scores)
        if roll == 1:
            print('Turn ' + str(t))
            print('Rolling...')
            print('Player ' + str(i) + ', you rolled a one your turn is over.')
            temp_score = 0
            if i == num_of_players:
                i = 1
                t += 1
            else:
                i += 1
                t += 1
        else:
            print('Turn ' + str(t))
            print('Rolling...')
            temp_score += roll
            cmmd = input('PLayer ' + str(i) + ', you rolled a ' + str(roll) + \
                         ' would you like to roll again?\n')
            while cmmd != 'no':
                print(cmmd)
                roll_2 = random.randint(1, 6)
                if roll_2 == 1:
                    print(player_scores)
                    print('Player ' + str(i) + ', you rolled a one your turn is over.')
                    cmmd = 'no'
                    temp_score = 0
                    if i == num_of_players:
                        i = 1
                        t += 1
                    else:
                        i += 1
                        t += 1
                else:
                    print(player_scores)
                    print('Turn ' + str(t))
                    print('Rolling...')
                    temp_score += roll_2
                    cmmd = input('PLayer ' + str(i) + ', you rolled a ' + str(roll_2) + \
                                ' would you like to roll again?\n')
            player_scores[i-1] += temp_score
            if i == num_of_players:
                i = 1
                t += 1
            else:
                i += 1
                t += 1
            temp_score = 0



main()
