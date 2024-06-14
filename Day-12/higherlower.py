import random

number_to_guess = random.randint(1,100)

user_reply = str(input("Do you want easy mode or hard mode?: (easy/hard)").lower())
if user_reply == "easy":
    number_of_lives = 10
else:
    number_of_lives = 5

while number_of_lives != 0:
    user_sol = int(input("Enter a number: "))
    if user_sol > number_to_guess:
        print("Lower")
        number_of_lives -= 1
        print(f"You have {number_of_lives} lives left")
    elif user_sol < number_to_guess:
        print("Higher")
        number_of_lives -= 1
        print(f"You have {number_of_lives} lives left")
    elif user_sol == number_to_guess:
        print("You win!")
        break
    if number_of_lives == 0:
        print("You lose")
        break