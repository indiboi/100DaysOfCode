import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

print("Enter the number of alphabets you want in your password:")
alpha = int(input())
print("Enter the number of digits you want in your password:")
dig = int(input())
print("Enter the number of symbols you want in yourpassword:")
symb = int(input())

password_list = []

for char in range(1, alpha+1):
    password_list += random.choice(alphabets)
for digit in range(1, dig+1):
    password_list += random.choice(digits)
for symbol in range(1, symb+1):
    password_list += random.choice(symbols)

random.shuffle(password_list)
password = ''
for i in password_list:
    password += i
print(password)



