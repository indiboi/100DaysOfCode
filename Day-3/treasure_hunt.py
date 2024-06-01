print("You have reached a cross road, choose either left or right: (type 'left' or 'right')")
choice1 = str(input())
if choice1 == 'left':
    print("You have reached a river, do you choose to swim or wait for a passerby on a boat? (type 'swim' or 'wait')")
    choice2 = str(input())
    if choice2 == 'swim':
        print("The current was too strong and you drown. GAME OVER!")
    elif choice2 == 'wait':
        print("While you were waiting for a passerby, a wild animal attacks you. GAME OVER!")
    else:
        print("Invalid choice, you get crushed by an asteroid. GAME OVER!")
elif choice1 == 'right':
    print("You find two cabins, one is rundown and one is sparky clean, which one do you enter? (type 'rundown' or 'clean')")
    choice3 = str(input())
    if choice3 == 'clean':
        print("All those glitters are not gold, you run into a serial killer and get murderd. GAME OVER!")
    elif choice3 == 'dirty':
        print("There are 3 doors in front of you with the faces of 3 artists - Drake, Kendrick Lamar and Metro Boomin. (type 'drake' or 'kendrick' or 'metro' to enter a room):")
        choice4 = str(input())
        if choice4 == 'drake':
            print("Wrong choice PEDO, GAME OVER!")
        elif choice4 == 'kendrick':
            print("Good choice but still wrong, GAME OVER!")
        elif choice4 == 'metro':
            print("GOOD CHOICE YOU WIN $4 BILLION WITH A 'B', CONGRATULATION!")
        else:
            print("WRONG CHOICE, GAME OVER!")
    else:
        print("Invalid answer, you get crushed by an asteroid. GAME OVER!")
else:
        print("Invalid answer, you get crushed by an asteroid. GAME OVER!")
