#this function use to additon of given number
def addition(a,b):
    sum = a+b
    return sum
#this function use to subtraction of given number
def subtraction(a,b):
    return a-b
#this function use to multiplication of given number
def multiplication(a,b):
    return a*b 
#this function use to divide of given number
def divide(a,b):
    return a/b
print("Please select your operation - \n"\
    "1. Addition\n"\
    "2. Subtraction\n"\
    "3. Multiplication\n"\
    "4. Divide\n")
while True:
    op = input("Enter your choice: ")
    
    a = int(input("enter your integer: "))
    b = int(input("enter your integer: "))

    if op == 1:
        print("The sum of integers is ",addition(a,b))
    elif op == 2:
        print("The subtraction of integers is ", subtraction(a,b))
    elif op == 3:
        print("The multiplication of integers is ", multiplication(a,b))
    elif op == 4:
        print("The divide of integers is ", divide(a,b))
    else:
        print("invalid")
            