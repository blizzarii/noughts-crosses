import random
import time
# 3 extra 10 cards to represent face cards
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,]

def hand_total(cards):
    aces = 0
    total = 0
    for value in cards:
        total = total + value
        # since aces can either be 1 or 11 ive written the function to be able to determine when an ace that is 11 should turn into a 1 when the total hand value is >21
        if value == 11:
            aces = aces + 1
    while total > 21 and aces > 0:
        total = total - 10
        aces = aces - 1
    return total

def hand_reveal():
    print("your hand:\n" + str(player_hand))
    time.sleep(1)
    print("total: " + str(hand_total(player_hand)))
# round start: starting hand is printed   

player_hand = [random.choice(deck), random.choice(deck)]
hand_reveal()
#user input
move = input("hit or stand?: ")
move = move.lower()
if move == "hit":
    player_hand.append(random.choice(deck))
    hand_reveal()
