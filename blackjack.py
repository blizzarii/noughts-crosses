import random
import time

win = 21
p_card1 = random.randint(1, 11)
p_card2 = random.randint(1, 11)
p_hand = p_card1 + p_card2
print("your current hand: ", p_hand)
time.sleep(1)
if p_hand == 21:
    print("you WIN!")
else:
    d_card1 = random.randint(1,11)
    d_card2 = random.randint(1,10)
    print("the dealer has: ", d_card1)
    choice_1 = input("HIT or STAND?: ")
    choice_1 = choice_1.upper()
    if choice_1 == "HIT":
        p_card3 = random.randint(1,11)
        p_hand = p_hand + p_card3
        print("your current hand: ", p_hand)
        if p_hand >21:
                print("you LOSE!")
        else:
             pass
    elif choice_1 == "STAND":
         choice_2 = input("HIT or STAND?: ")
         choice_2 = choice_2.upper()
         if choice_2 == "HIT":
                 p_card3 = random.randint(1,11)
                 p_hand = p_hand + p_card3
                 print("your current hand: ", p_hand)
         elif choice_2 == "STAND":
                 #the dealer flips his hidden card and hits until he gets a higher number than the player
                 d_hand = d_card1
                 print("the dealer's current hand: ", d_hand)
                 d_hand = d_hand + d_card2
                 print("the card flips.. his total is now.. ", d_hand)
                 while d_hand <21 and d_hand <p_hand:
                       d_card_showdown = random.randint(1,11)
                       d_hand = d_hand + d_card_showdown
                       print("the dealer's total: ", d_hand)
                       

                 if p_hand >21:
                         print("you LOSE!")
         
    else:
          print("invalid")