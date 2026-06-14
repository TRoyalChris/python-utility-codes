from os import system

num = 1
bid_amounts = {}
finish = False
print("Welcome to the secret bid game")
highest_Bid = 0
highest_bidder = ""

while not finish:
    key = input(f"Please input the name of the bidder #{num}: ")
    value = int(input(f"Please input the amount to bid: $"))
    bid_amounts[key] = value
    nextPerson = input("Is there any other bidder? Y/N: ").lower()
    if nextPerson == "y":
        system("cls")
        num += 1
    elif nextPerson == "n":
        system("cls")
        finish = True
        for keys in bid_amounts:
            if bid_amounts[keys] > highest_Bid:
                highest_Bid = bid_amounts[keys]
                highest_bidder = keys
        print(bid_amounts)
        print(f"The Highest Bid is {highest_bidder} with a bid of ${highest_Bid}")

    else:
        print("Please enter either 'y' or 'n', either way well continue for now...")
        system("cls")
        num += 1


