def Armstrong(n):
    sum = 0
    x = n
    while n>0: 
        a = n%10
        sum = sum  + a**3
        n//=10
    if sum==x:
        print ("Number is Armstrong")
        return sum
    else:
        print("number is not Armstrong")
n = int(input("Enter the number: "))
result = Armstrong(n)
print("Armstrong number is: ", Armstrong(n))