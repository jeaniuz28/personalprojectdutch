import random
import time

cards = []
discard_pile = []
game_over = False
stack1ran = False
stack2ran = False

suits = ["♣", "♦", "♥", "♠"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

for suit in suits:
    for rank in ranks:
        #append = adding elements at the end of a list
        cards.append("".join([rank, suit]))

#shuffling cards
def shuffle_cards():
    random.shuffle(cards)

def deal_card(number_of_cards):
    #empty list to hold dealt cards
    cards_dealt = []
    for i in range(number_of_cards):
        #remove last card from deck and store it
        card = cards.pop()
        #append dealt cards to cards_dealt list
        cards_dealt.append(card)
    if number_of_cards == 1:
        return cards_dealt[0]
    return cards_dealt

#function to calculate the point or the value of each hand
def get_value(hand):
    #initializing total values as 0
    value = 0
    #loop through each card in each hand
    for card in hand:
        rank = card[0]
        suit = card[1]
        if rank == "A":
            value += 1
        elif rank in ["J", "Q"]:
            value += 13
        elif rank == "K" and suit in ["♣", "♠"]:
            value =+ 13
        elif rank == "K" and suit in ["♦", "♥"]:
            value += 0
        elif rank == "1" and suit == "0":
            value += 10
        else:
            value += int(rank)
    return value

shuffle_cards()

player1_hand = deal_card(4)
player2_hand = deal_card(4)

display1 = []
for card in player1_hand:
    display1 += "_"
display2 = []
for card in player2_hand:
    display2 += "_"


print("Player 1, your cards are:", display1)
print("Player 2, your cards are:", display2)

first_card_reveal1 = input("Are you ready to see 2 of your cards player 1? ").lower()
if first_card_reveal1 == "yes":
    display1[:2] = player1_hand[:2]
    print(display1)
else:
    print("Say 'yes'.")
    first_card_reveal1 = input("Are you ready to see 2 of your cards player 1? ").lower()
    if first_card_reveal1 == "yes":
        display1[:2] = player1_hand[:2]
        print(display1)

# time.sleep(5)
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
print("Player 1, make sure you scroll so that player 2 can't see your first two cards.")

first_card_reveal2 = input("Are you ready to see 2 of your cards player 2? ").lower()
if first_card_reveal2 == "yes":
    display2[:2] = player2_hand[:2]
    print(display2)
else:
    print("say 'yes'.")
    first_card_reveal2 = input("Are you ready to see 2 of your cards player 2? ").lower()
    if first_card_reveal2 == "yes":
        display2[:2] = player2_hand[:2]
        print(display2)

# time.sleep(5)
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
print("Player 2, make sure you scroll so that player 1 can't see your first two cards.")


# time.sleep(2)
def turn1():
    global game_over, player1_hand
    def validator():
        valid = False
        while not valid:
            choice = input("What would you like to do with it: discard, swap1, swap2, swap3, or swap4?> ").lower()
            if choice == "discard":
                valid = True
                return "discard"
            elif len(choice) == 5 and int(choice[4]) <= len(player1_hand):
                valid = True
                return choice
            else:
                print("You don't have enough cards, try again.")
    pick_up = input("Now, player 1, are you ready to pick up a card? ").lower()
    if pick_up == "yes":
        picked_up = deal_card(1)
        print("Your card is: %s" % picked_up)
        action = validator()
        if action == "discard":
            discard_pile.append(picked_up)
            print("Ok. Card discarded.")
        elif action == "swap1":
            print("Ok. You swapped out: %s" % player1_hand[0])
            discard_pile.append(player1_hand[0])
            player1_hand[0] = picked_up
        elif action == "swap2":
            print("Ok. You swapped out: %s" % player1_hand[1])
            discard_pile.append(player1_hand[1])
            player1_hand[1] = picked_up
        elif action == "swap3":
            print("Ok. You swapped out: %s" % player1_hand[2])
            discard_pile.append(player1_hand[2])
            player1_hand[2] = picked_up
        elif action == "swap4":
            print("Ok. You swapped out: %s" % player1_hand[3])
            discard_pile.append(player1_hand[3])
            player1_hand[3] = picked_up
        else:
            print("Please answer within the given choices. The turn will now be restarting.")
            turn1()
    else:
        print("Say 'yes' player 1.")
        turn1()
    if len(discard_pile) != 0:
        stack1()
        if stack1ran == True:
            facecard1()
        stack2()
        if stack2ran == True:
            facecard2()
    facecard1()
    dutch()
    if game_over == True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        lastturn2()
        result_calc()
    return

def turn2():
    global game_over, player2_hand
    def validator():
        valid = False
        while not valid:
            choice = input("What would you like to do with it: discard, swap1, swap2, swap3, or swap4?> ").lower()
            if choice == "discard":
                valid = True
                return "discard"
            elif len(choice) == 5 and int(choice[4]) <= len(player2_hand):
                valid = True
                return choice
            else:
                print("You don't have enough cards, try again.")
    pick_up = input("Now, player 2, are you ready to pick up a card? ").lower()
    if pick_up == "yes":
        picked_up = deal_card(1)
        print("Your card is: %s" % picked_up)
        action = validator()
        if action == "discard":
            discard_pile.append(picked_up)
            print("Ok. Card discarded.")
        elif action == "swap1":
            print("Ok. You swapped out: %s" % player2_hand[0])
            discard_pile.append(player2_hand[0])
            player2_hand[0] = picked_up
        elif action == "swap2":
            print("Ok. You swapped out: %s" % player2_hand[1])
            discard_pile.append(player2_hand[1])
            player2_hand[1] = picked_up
        elif action == "swap3":
            print("Ok. You swapped out: %s" % player2_hand[2])
            discard_pile.append(player2_hand[2])
            player2_hand[2] = picked_up
        elif action == "swap4":
            print("Ok. You swapped out: %s" % player2_hand[3])
            discard_pile.append(player2_hand[3])
            player2_hand[3] = picked_up
        else:
            print("Please answer within the given choices. The turn will now be restarting.")
            turn2()
    else:
        print("Say 'yes' player 2.")
        turn2()
    if len(discard_pile) != 0:
        stack2()
        if stack2ran == True:
            facecard2()
        stack1()
        if stack1ran == True:
            facecard1()
    facecard2()
    dutch()
    if game_over == True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        lastturn1()
        result_calc()
    return

def lastturn1():
    global game_over, player1_hand
    def validator():
        valid = False
        while not valid:
            choice = input("What would you like to do with it: discard, swap1, swap2, swap3, or swap4?> ").lower()
            if choice == "discard":
                valid = True
                return "discard"
            elif len(choice) == 5 and int(choice[4]) <= len(player1_hand):
                valid = True
                return choice
            else:
                print("You don't have enough cards, try again.")
    pick_up = input("Now, player 1, it is your last turn. Ready to pick up a card? ").lower()
    if pick_up == "yes":
        picked_up = deal_card(1)
        print("Your card is: %s" % picked_up)
        action = validator()
        if action == "discard":
            discard_pile.append(picked_up)
            print("Ok. Card discarded.")
        elif action == "swap1":
            print("Ok. You swapped out: %s" % player1_hand[0])
            discard_pile.append(player1_hand[0])
            player1_hand[0] = picked_up
        elif action == "swap2":
            print("Ok. You swapped out: %s" % player1_hand[1])
            discard_pile.append(player1_hand[1])
            player1_hand[1] = picked_up
        elif action == "swap3":
            print("Ok. You swapped out: %s" % player1_hand[2])
            discard_pile.append(player1_hand[2])
            player1_hand[2] = picked_up
        elif action == "swap4":
            print("Ok. You swapped out: %s" % player1_hand[3])
            discard_pile.append(player1_hand[3])
            player1_hand[3] = picked_up
        else:
            print("Please answer within the given choices. The turn will now be restarting.")
            lastturn1()
    if len(discard_pile) != 0:
        stack1()
        if stack1ran == True:
            facecard1()
        stack2()
        if stack2ran == True:
            facecard2()
    else:
        print("Say 'yes' player 1.")
        lastturn1()
    facecard1()
    return

def lastturn2():
    global game_over, player2_hand
    def validator():
        valid = False
        while not valid:
            choice = input("What would you like to do with it: discard, swap1, swap2, swap3, or swap4?> ").lower()
            if choice == "discard":
                valid = True
                return "discard"
            elif len(choice) == 5 and int(choice[4]) <= len(player2_hand):
                valid = True
                return choice
            else:
                print("You don't have enough cards, try again.")
    pick_up = input("Now, player 2, it is your last turn. Ready to pick up a card? ").lower()
    if pick_up == "yes":
        picked_up = deal_card(1)
        print("Your card is: %s" % picked_up)
        action = validator()
        if action == "discard":
            discard_pile.append(picked_up)
            print("Ok. Card discarded.")
        elif action == "swap1":
            print("Ok. You swapped out: %s" % player2_hand[0])
            discard_pile.append(player2_hand[0])
            player2_hand[0] = picked_up
        elif action == "swap2":
            print("Ok. You swapped out: %s" % player2_hand[1])
            discard_pile.append(player2_hand[1])
            player2_hand[1] = picked_up
        elif action == "swap3":
            print("Ok. You swapped out: %s" % player2_hand[2])
            discard_pile.append(player2_hand[2])
            player2_hand[2] = picked_up
        elif action == "swap4":
            print("Ok. You swapped out: %s" % player2_hand[3])
            discard_pile.append(player2_hand[3])
            player2_hand[3] = picked_up
        else:
            print("Please answer within the given choices. The turn will now be restarting.")
            lastturn2()
    if len(discard_pile) != 0:
        stack2()
        if stack2ran == True:
            facecard2()
        stack1()
        if stack1ran == True:
            facecard1()
    else:
        print("Say 'yes' player 2.")
        lastturn2()
    facecard2()
    return

def stack2():
    global player2_hand, discard_pile, stack2ran
    stack2ran = False
    last_discard = discard_pile[-1]
    discard_rank = last_discard[0]
    stack_on_1 = input("Player 2, you can stack one of your cards on top of the discard pile if you have the same card. Which card would you like to stack: 1, 2, 3, 4, or none? > ").lower()
    if stack_on_1 == "none":
        return
    elif stack_on_1 == "1":
        player2_card1 = player2_hand[0]
        print("You just discarded: %s" % player2_hand[0])
        player2_hand.remove(player2_card1)
        if player2_card1[0] == discard_rank:
            print("Good job! The cards' ranks matched. Now you only have %d cards left" % len(player2_hand))
        else:
            player2_hand.append(deal_card(1))
            print("I don't think the ranks matched.. Here's a card for your penalty. Now you have %d cards left. The card is added as your last card. " % len(player2_hand))
        stack2ran = True
    elif stack_on_1 == "2":
        player2_card2 = player2_hand[1]
        print("You just discarded: %s" % player2_hand[1])
        player2_hand.remove(player2_card2)
        if player2_card2[0] == discard_rank:
            print("Good job! The cards' ranks matched. Now you only have %d cards left" % len(player2_hand))
        else:
            player2_hand.append(deal_card(1))
            print("I don't think the ranks matched.. Here's a card for your penalty. Now you have %d cards left. The card is added as your last card. " % len(
                player2_hand))
        stack2ran = True
    elif stack_on_1 == "3":
        player2_card3 = player2_hand[2]
        print("You just discarded: %s" % player2_hand[2])
        player2_hand.remove(player2_card3)
        if player2_card3[0] == discard_rank:
            print("Good job! The cards' ranks matched. Now you only have %d cards left" % len(player2_hand))
        else:
            player2_hand.append(deal_card(1))
            print("I don't think the ranks matched.. Here's a card for your penalty. Now you have %d cards left. The card is added as your last card. " % len(
                player2_hand))
        stack2ran = True
    elif stack_on_1 == "4":
        player2_card4 = player2_hand[3]
        print("You just discarded: %s" % player2_hand[3])
        player2_hand.remove(player2_card4)
        if player2_card4[0] == discard_rank:
            print("Good job! The cards' ranks matched. Now you only have %d cards left" % len(player2_hand))
        else:
            player2_hand.append(deal_card(1))
            print("I don't think the ranks matched.. Here's a card for your penalty. Now you have %d cards left. The card is added as your last card. " % len(
                player2_hand))
        stack2ran = True
    return player2_hand

def stack1():
    global player1_hand, discard_pile, stack1ran
    last_discard = discard_pile[-1]
    discard_rank = last_discard[0]
    stack_on_2 = input("Player 1, you can stack one of your cards on top of the discard pile if you have the same card. Which card would you like to stack: 1, 2, 3, 4, or none? > ").lower()
    stack1ran = False
    if stack_on_2 == "none":
        return
    elif stack_on_2 == "1":
        player1_card1 = player1_hand[0]
        print("You just discarded: %s" % player1_hand[0])
        player1_hand.remove(player1_card1)
        if player1_card1[0] == discard_rank:
            print("Good job! The cards' ranks matched. Now you only have %d cards left" % len(player1_hand))
        else:
            player1_hand.append(deal_card(1))
            print("I don't think the ranks matched.. Here's a card for your penalty. Now you have %d cards left. The card is added as your last card. " % len(player1_hand))
        stack1ran = True
    elif stack_on_2 == "2":
        player1_card2 = player1_hand[1]
        print("You just discarded: %s" % player1_hand[1])
        player1_hand.remove(player1_card2)
        if player1_card2[0] == discard_rank:
            print("Good job! The cards' ranks matched. Now you only have %d cards left" % len(player1_hand))
        else:
            player1_hand.append(deal_card(1))
            print("I don't think the ranks matched.. Here's a card for your penalty. Now you have %d cards left. The card is added as your last card. " % len(
                player1_hand))
        stack1ran = True
    elif stack_on_2 == "3":
        player1_card3 = player1_hand[2]
        print("You just discarded: %s" % player1_hand[2])
        player1_hand.remove(player1_card3)
        if player1_card3[0] == discard_rank:
            print("Good job! The cards' ranks matched. Now you only have %d cards left" % len(player1_hand))
        else:
            player1_hand.append(deal_card(1))
            print("I don't think the ranks matched.. Here's a card for your penalty. Now you have %d cards left. The card is added as your last card. " % len(
                player1_hand))
        stack1ran = True
    elif stack_on_2 == "4":
        player1_card4 = player1_hand[3]
        print("You just discarded: %s" % player1_hand[3])
        player1_hand.remove(player1_card4)
        if player1_card4[0] == discard_rank:
            print("Good job! The cards' ranks matched. Now you only have %d cards left" % len(player1_hand))
        else:
            player1_hand.append(deal_card(1))
            print("I don't think the ranks matched.. Here's a card for your penalty. Now you have %d cards left. The card is added as your last card. " % len(
                player1_hand))
        stack1ran = True
    return player1_hand

def dutch():
    global game_over
    dutch_or_nah = input("Dutch? > ").lower()
    if dutch_or_nah == "yes":
        game_over = True
    elif dutch_or_nah == "no":
        game_over = False
    else:
        print("Say 'yes' or 'no'")
        dutch()

def result_calc():
    global player1_hand, player2_hand
    print("Player 1, your cards were: ", player1_hand)
    print("Player 2, your cards were:", player2_hand)
    player1_final_score = get_value(player1_hand)
    player2_final_score = get_value(player2_hand)
    print("Player 1, your score were:", player1_final_score)
    print("Player 2, your score were:", player2_final_score)
    if player1_final_score < player2_final_score:
        print("Good job player 1!! You won.")
        return
    elif player2_final_score < player1_final_score:
        print("Good job player 2!! You won.")
        return
    elif player1_final_score == player2_final_score:
        print("You guys tied!! Woah that's rare.")
        return

def facecard1():
    global discard_pile, player1_hand, player2_hand
    last_discard = discard_pile[-1]
    discard_rank = last_discard[0]
    discard_suit = last_discard[1]
    if discard_rank == "Q":
        def queenvalidator():
            queenspecial = input("Queen allows you to view one of your card. Which card would you like to view: 1, 2, 3, 4, or none? > ")
            if queenspecial == "none":
                return
            elif len(queenspecial) == 1 and int(queenspecial) <= len(player1_hand):
                if queenspecial == "1":
                    print("This is your card:", player1_hand[0])
                elif queenspecial == "2":
                    print("This is your card:", player1_hand[1])
                elif queenspecial == "3":
                    print("This is your card:", player1_hand[2])
                elif queenspecial == "4":
                    print("This is your card:", player1_hand[3])
            elif len(queenspecial) == 1 and int(queenspecial) >= len(player1_hand):
                print("You don't have enough cards, try again.")
                queenvalidator()
            else:
                print("Please answer within the option.")
                queenvalidator()
        queenvalidator()
    elif discard_rank == "K" and (discard_suit == "♠" or discard_suit == "♣"):
        print("You just play a black king. You get one more turn!")
        turn1()
    elif discard_rank == "J":
        def jackvalidator():
            jackspecial = input("Jack allow you to swap one of your card with the other player. Which one of YOUR CARD would you like to swap: 1, 2, 3, 4, or none? > ")
            if jackspecial == "none":
                return
            elif len(jackspecial) == 1 and int(jackspecial) <= len(player1_hand):
                def jackvalidator2():
                    jackspecial2 = input("Which one of player 2 card would you like to swap with: 1, 2, 3, or 4? > ")
                    if len(jackspecial2) == 1 and int(jackspecial2) <= len(player2_hand):
                        if jackspecial2 == "1":
                            card2 = player2_hand[0]
                            player2_hand.remove(player2_hand[0])
                            if jackspecial == "1":
                                card1 = player1_hand[0]
                                player1_hand.remove(player1_hand[0])
                                player1_hand.insert(0, card2)
                                player2_hand.insert(0, card1)
                            elif jackspecial == "2":
                                card1 = player1_hand[1]
                                player1_hand.remove(player1_hand[1])
                                player1_hand.insert(1, card2)
                                player2_hand.insert(0, card1)
                            elif jackspecial == "3":
                                card1 = player1_hand[2]
                                player1_hand.remove(player1_hand[2])
                                player1_hand.insert(2, card2)
                                player2_hand.insert(0, card1)
                            elif jackspecial == "4":
                                card1 = player1_hand[3]
                                player1_hand.remove(player1_hand[3])
                                player1_hand.insert(3, card2)
                                player2_hand.insert(0, card1)
                        elif jackspecial2 == "2":
                            card2 = player2_hand[1]
                            player2_hand.remove(player2_hand[1])
                            if jackspecial == "1":
                                card1 = player1_hand[0]
                                player1_hand.remove(player1_hand[0])
                                player1_hand.insert(0, card2)
                                player2_hand.insert(1, card1)
                            elif jackspecial == "2":
                                card1 = player1_hand[1]
                                player1_hand.remove(player1_hand[1])
                                player1_hand.insert(1, card2)
                                player2_hand.insert(1, card1)
                            elif jackspecial == "3":
                                card1 = player1_hand[2]
                                player1_hand.remove(player1_hand[2])
                                player1_hand.insert(2, card2)
                                player2_hand.insert(1, card1)
                            elif jackspecial == "4":
                                card1 = player1_hand[3]
                                player1_hand.remove(player1_hand[3])
                                player1_hand.insert(3, card2)
                                player2_hand.insert(1, card1)
                        elif jackspecial2 == "3":
                            card2 = player2_hand[2]
                            player2_hand.remove(player2_hand[2])
                            if jackspecial == "1":
                                card1 = player1_hand[0]
                                player1_hand.remove(player1_hand[0])
                                player1_hand.insert(0, card2)
                                player2_hand.insert(2, card1)
                            elif jackspecial == "2":
                                card1 = player1_hand[1]
                                player1_hand.remove(player1_hand[1])
                                player1_hand.insert(1, card2)
                                player2_hand.insert(2, card1)
                            elif jackspecial == "3":
                                card1 = player1_hand[2]
                                player1_hand.remove(player1_hand[2])
                                player1_hand.insert(2, card2)
                                player2_hand.insert(2, card1)
                            elif jackspecial == "4":
                                card1 = player1_hand[3]
                                player1_hand.remove(player1_hand[3])
                                player1_hand.insert(3, card2)
                                player2_hand.insert(2, card1)
                        elif jackspecial2 == "4":
                            card2 = player2_hand[3]
                            player2_hand.remove(player2_hand[3])
                            if jackspecial == "1":
                                card1 = player1_hand[0]
                                player1_hand.remove(player1_hand[0])
                                player1_hand.insert(0, card2)
                                player2_hand.insert(3, card1)
                            elif jackspecial == "2":
                                card1 = player1_hand[1]
                                player1_hand.remove(player1_hand[1])
                                player1_hand.insert(1, card2)
                                player2_hand.insert(3, card1)
                            elif jackspecial == "3":
                                card1 = player1_hand[2]
                                player1_hand.remove(player1_hand[2])
                                player1_hand.insert(2, card2)
                                player2_hand.insert(3, card1)
                            elif jackspecial == "4":
                                card1 = player1_hand[3]
                                player1_hand.remove(player1_hand[3])
                                player1_hand.insert(3, card2)
                                player2_hand.insert(3, card1)
                    elif len(jackspecial2) == 1 and int(jackspecial2) >= len(player2_hand):
                        print("Player 2 doesn't have enough cards, try again.")
                        jackvalidator2()
                    else:
                        print("Please answer within the options, try again.")
                        jackvalidator2()
                jackvalidator2()
            elif len(jackspecial) == 1 and int(jackspecial) >= len(player1_hand):
                print("You don't have enough cards, try again.")
                jackvalidator()
            else:
                print("Please answer within the options.")
                jackvalidator()
        jackvalidator()
    else:
        return

def facecard2():
    global discard_pile, player1_hand, player2_hand
    last_discard = discard_pile[-1]
    discard_rank = last_discard[0]
    discard_suit = last_discard[1]
    if discard_rank == "Q":
        def queenvalidator():
            queenspecial = input(
                "Queen allows you to view one of your card. Which card would you like to view: 1, 2, 3, 4, or none? > ")
            if queenspecial == "none":
                return
            elif len(queenspecial) == 1 and int(queenspecial) <= len(player2_hand):
                if queenspecial == "1":
                    print("This is your card:", player2_hand[0])
                elif queenspecial == "2":
                    print("This is your card:", player2_hand[1])
                elif queenspecial == "3":
                    print("This is your card:", player2_hand[2])
                elif queenspecial == "4":
                    print("This is your card:", player2_hand[3])
            elif len(queenspecial) == 1 and int(queenspecial) >= len(player2_hand):
                print("You don't have enough cards, try again.")
                queenvalidator()
            else:
                print("Please answer within the option.")
                queenvalidator()
        queenvalidator()
    elif discard_rank == "K" and (discard_suit == "♠" or discard_suit == "♣"):
        print("You just play a black king. You get one more turn!")
        turn2()
    elif discard_rank == "J":
        def jackvalidator():
            jackspecial = input("Jack allow you to swap one of your card with the other player. Which one of YOUR CARD would you like to swap: 1, 2, 3, 4, or none? > ")
            if jackspecial == "none":
                return
            elif len(jackspecial) == 1 and int(jackspecial) <= len(player2_hand):
                def jackvalidator2():
                    jackspecial1 = input("Which one of player 1 card would you like to swap with: 1, 2, 3, or 4? > ")
                    if int(jackspecial1) <= len(player1_hand):
                        if jackspecial1 == "1":
                            card1 = player1_hand[0]
                            player1_hand.remove(player1_hand[0])
                            if jackspecial == "1":
                                card2 = player2_hand[0]
                                player2_hand.remove(player2_hand[0])
                                player2_hand.insert(0, card1)
                                player1_hand.insert(0, card2)
                            elif jackspecial == "2":
                                card2 = player2_hand[1]
                                player2_hand.remove(player2_hand[1])
                                player2_hand.insert(1, card1)
                                player1_hand.insert(0, card2)
                            elif jackspecial == "3":
                                card2 = player2_hand[2]
                                player2_hand.remove(player2_hand[2])
                                player2_hand.insert(2, card1)
                                player1_hand.insert(0, card2)
                            elif jackspecial == "4":
                                card2 = player2_hand[3]
                                player2_hand.remove(player2_hand[3])
                                player2_hand.insert(3, card1)
                                player1_hand.insert(0, card2)
                        elif jackspecial1 == "2":
                            card1 = player1_hand[1]
                            player1_hand.remove(player1_hand[1])
                            if jackspecial == "1":
                                card2 = player2_hand[0]
                                player2_hand.remove(player2_hand[0])
                                player2_hand.insert(0, card1)
                                player1_hand.insert(1, card2)
                            elif jackspecial == "2":
                                card2 = player2_hand[1]
                                player2_hand.remove(player2_hand[1])
                                player2_hand.insert(1, card1)
                                player1_hand.insert(1, card2)
                            elif jackspecial == "3":
                                card2 = player2_hand[2]
                                player2_hand.remove(player2_hand[2])
                                player2_hand.insert(2, card1)
                                player1_hand.insert(1, card2)
                            elif jackspecial == "4":
                                card2 = player2_hand[3]
                                player2_hand.remove(player2_hand[3])
                                player2_hand.insert(3, card1)
                                player1_hand.insert(1, card2)
                        elif jackspecial1 == "3":
                            card1 = player1_hand[2]
                            player1_hand.remove(player1_hand[2])
                            if jackspecial == "1":
                                card2 = player2_hand[0]
                                player2_hand.remove(player2_hand[0])
                                player2_hand.insert(0, card1)
                                player1_hand.insert(2, card2)
                            elif jackspecial == "2":
                                card2 = player2_hand[1]
                                player2_hand.remove(player2_hand[1])
                                player2_hand.insert(1, card1)
                                player1_hand.insert(2, card2)
                            elif jackspecial == "3":
                                card2 = player2_hand[2]
                                player2_hand.remove(player2_hand[2])
                                player2_hand.insert(2, card1)
                                player1_hand.insert(2, card2)
                            elif jackspecial == "4":
                                card2 = player2_hand[3]
                                player2_hand.remove(player2_hand[3])
                                player2_hand.insert(3, card1)
                                player1_hand.insert(2, card2)
                        elif jackspecial1 == "4":
                            card1 = player1_hand[3]
                            player1_hand.remove(player1_hand[3])
                            if jackspecial == "1":
                                card2 = player2_hand[0]
                                player2_hand.remove(player2_hand[0])
                                player2_hand.insert(0, card1)
                                player1_hand.insert(3, card2)
                            elif jackspecial == "2":
                                card2 = player2_hand[1]
                                player2_hand.remove(player2_hand[1])
                                player2_hand.insert(1, card1)
                                player1_hand.insert(3, card2)
                            elif jackspecial == "3":
                                card2 = player2_hand[2]
                                player2_hand.remove(player2_hand[2])
                                player2_hand.insert(2, card1)
                                player1_hand.insert(3, card2)
                            elif jackspecial == "4":
                                card2 = player2_hand[3]
                                player2_hand.remove(player2_hand[3])
                                player2_hand.insert(3, card1)
                                player1_hand.insert(3, card2)
                    elif int(jackspecial1) >= len(player1_hand):
                        print("Player 1 doesn't have enough cards. Try again.")
                        jackvalidator2()
                    else:
                        print("PLease answer within the options.")
                        jackvalidator2()
                jackvalidator2()
            elif len(jackspecial) == 1 and int(jackspecial) >= len(player2_hand):
                print("You don't have enough cards, try again.")
                jackvalidator()
            else:
                print("Please answer within the options.")
                jackvalidator()
        jackvalidator()
    else:
        return

while not game_over:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    turn1()
    if game_over:
        break
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    turn2()
    if game_over:
        break