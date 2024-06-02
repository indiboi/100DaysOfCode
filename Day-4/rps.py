import random

print("Enter 0, 1 or 2 for rock paper or scissor respectfully:")
x = int(input())
y = random.randint(0,2)
choice = ["Rock", "Paper", "Scissor"]
if x == 0 and y == 0 or x == 1 and y == 1 or x == 2 and y == 2:
    print(f"The computer picked {choice[y]} and you picked {choice[x]}, hence its a draw")
elif x == 0 and y == 2 or x == 1 and y == 0 or x == 2 and y == 1:
    print(f"The computer picked {choice[y]} and you picked {choice[x]}, hence you win!")
else:
    print(f"The computer picked {choice[y]} and you picked {choice[x]}, hence the computer wins!")