#!/usr/bin/env python3
#create a function for calculate a factorial of a number
def factorial(n):
    #define condition
    if n==0:
        return 1
    #logic to calculate factorial
    return n * factorial(n-1)
#Driver code
n= int(input("enter a number: "))
#strore the value of fzctorial in result
result = factorial(n)
print('The factorial is: ' , n,"-" , result)
