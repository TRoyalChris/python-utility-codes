def add(a,b):
    """This function adds two numbers together"""
    return a+b
def subtract(a,b):
    """This function subtracts two numbers together"""
    return a-b
def multiply(a,b):
    """This function multiplies two numbers together"""
    return a*b
def divide(a,b):
    """This function divides two numbers together"""
    return a/b

calc_used = True
result = 0
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
while calc_used:

    print("=" * 30 + "Python Calculator" + "=" * 30)
    if result == 0:
        first_number = int(input("Enter the first number:\n"))
    else:
        first_number = result
    operator = input(f"Enter the operator (+,-,*,/):\n").lower()
    second_number = int(input("Enter the second number:\n"))
    result = operations[operator](first_number, second_number)
    print("=" * 30)
    print(result)
    continue_using = input("Do you want to continue? (y/n)\n").lower()
    if continue_using == "y":
        new_num = input("Would you like to continue using the current result? (y/n)\n").lower()
        if new_num == "n":
            result = 0
        else:
            print("Perfect, well take this as a yes!")

    elif continue_using == "n":
        calc_used = False
    else:
        print("Not a valid option, goodbye")
        calc_used = False
