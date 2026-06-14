import random

# Lists for symbols and possible characters
alphabet_list = [
    'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g',
    'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n',
    'Ñ', 'ñ', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't',
    'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z'
]
numbers_list =  [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]
symbols_list = ['!','#','$','%','&','(',')','*','+']

# Password holder
password_list = []
password = ""

# User Input
print("Welcome to the password generator!")
num_letters = int(input("How many letters would you like?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

# Magic behind the scenes code
for letters in range(num_letters):
    password_list.append(random.choice(alphabet_list))
for symbols in range(num_symbols):
    password_list.append(random.choice(symbols_list))
for numbers in range(num_numbers):
    password_list.append(random.choice(numbers_list))

# Password shuffler
random.shuffle(password_list)
for letters in password_list:
    password += letters
print(f"You password is:\n{password}")

