# Write a program that takes two numbers and an operation (add, subtract, multiply, divide) and prints the result.
# Concepts: Variables, user input, conditionals.

# add x & y
def add(x,y):
    return(x + y)

# sub. x & y
def sub(x,y):
    return(x - y)

# mult. x & y
def mult(x,y):
    return(x * y)

# div. x & y
def div(x,y):
    return(x / y)

### main
while True:

    # ask what operator to use.
    while True:
        operator = input("What operator are you needing? ") 

        if operator in ["+","-","*","/"]:
            break

        print("Please use a operator that is avalible. + - * /")

    # get values for x and y
    x = int(input("what is x? "))
    y = int(input("what is y? "))

    # do the operation with values
    if operator == "+":
        print(add(x,y))
    elif operator == "-":
        print(sub(x, y))
    elif operator == "*":
        print(mult(x, y))
    else:
        print(div(x,y))

    # end program
    quit = input("Do you want to quit? ")
    if quit in ["yes", "Yes", "y", "Y"]:
        break
