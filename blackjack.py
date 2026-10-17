import random
import time
deck = [2, 3, 4, 5, 6, 7, 8]
player_hand = []
def hand_total(cards):
    aces = 0
    total = 0
    for value in cards:
        total = total + value
        #since aces can either be 1 or 11 ive written the function to be able to determine when an ace that is 11 should turn into a 1 when the total hand value is >21
        if value == 11:
            aces = aces + 1
    while total > 21 and aces > 0:
        total = total - 10
        aces = aces - 1
        return total
           
