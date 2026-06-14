import  string
#This imports a string of lower case letters
alphabet = list(string.ascii_lowercase)
close = False
cipher_banner = r"""
  ____                                 ____ _       _               
 / ___|__ _  ___  ___  __ _ _ __      / ___(_)_ __ | |__   ___ _ __ 
| |   / _` |/ _ \/ __|/ _` | '__|____| |   | | '_ \| '_ \ / _ \ '__|
| |__| (_| |  __/\__ \ (_| | | |_____| |___| | |_) | | | |  __/ |   
 \____\__,_|\___||___/\__,_|_|        \____|_| .__/|_| |_|\___|_|   
                                             |_|                    
"""
def placeLogo():
    print("=" * 68)
    print(cipher_banner)
    print("=" * 68)

placeLogo()

def encrypt(message, shift_amount ):
    new_message = ""
    for letter in message:
        if letter in alphabet:
            new_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            new_message += alphabet[new_position]
        elif letter not in alphabet:
            new_message += letter
    print(f"The {direction}d message is: {new_message}")

def decrypt(message, shift_amount ):
    new_message = ""
    for letter in message:
        if letter in alphabet:
            new_position = alphabet.index(letter) - shift_amount
            new_message += alphabet[new_position]
        elif letter not in alphabet:
            new_message += letter
    print(f"The {direction}d message is:\n{new_message}")

def ceasar(direction):
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Please type 'encode' or 'decode'")
while not close:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(direction)
    again = input("Would you like to use another message again? yes/no \n").lower()
    if again == "no":
        close = True
        print("Goodbye for now Human :D")
    elif again == "yes":
        print("\n"*50)
        print("=" * 68)
        print(cipher_banner)
        print("=" * 68)
    else:
        print("Please read >:c")



#ifmmp!