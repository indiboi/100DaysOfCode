import random 
import time

def hit(given_list):
    given_list.append(random.randint(1,10))

def total_value(given_list):
    total = 0
    for i in given_list:
        total += i
    return total

def check_total_value(given_list):
    sol = total_value(given_list)
    if sol > 21:
        return "bust"
    

user_cards = []
computer_cards = []
user_bust = False
computer_bust = False

continue_game = True
user_cards.append(random.randint(1,10))
user_cards.append(random.randint(1,10))
computer_cards.append(random.randint(1,10))

#users loop

while continue_game:
    print(f"Your cards are {user_cards} and their value is: {total_value(user_cards)}")
    print(f"The computers card is {computer_cards} and its total value is: {total_value(computer_cards)}")
    user_reply = str(input("Would you like to hit or leave? (hit/leave)").lower())
    if user_reply == "leave":
        continue_game = False
        break
    else:
        user_cards.append(random.randint(1,10))
        print(f"Your total value is {total_value(user_cards)}")
        if check_total_value(user_cards) == "bust":
            print("Your total is above 21")
            user_bust = True
            break
            
#computers loop

while True:
    if user_bust:
        break
    computer_cards.append(random.randint(1,10))
    print(f"Your cards are {user_cards} and their value is: {total_value(user_cards)}")
    print(f"The computers card is {computer_cards} and its total value is: {total_value(computer_cards)}")
    if(total_value(computer_cards) < total_value(user_cards) and total_value(computer_cards) < 15):
        computer_cards.append(random.randint(1,10))
        print(f"The total value of computers cards is {total_value(computer_cards)}")
        time.sleep(3)
        if(check_total_value(computer_cards) == "bust"):
            print("The computers total is above 21")
            computer_bust = True
            break
    else:
        break


if computer_bust or user_bust:
    if computer_bust:
        print("The computer bust, you win")
    else:
        print("You bust, the computer wins")
else:
    if total_value(user_cards) > total_value(computer_cards):
        print(f"Your total value is {total_value(user_cards)} and you win")
    else:
        print(f"The computers total value is {total_value(computer_cards)} and the computer wins")
