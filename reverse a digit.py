#create a fuction for calculate a reverse a number
def reverse(n):
    rev = 0
    #conditional loop when n>0 then store value in rev
    while n>0:
        a = n%10
        rev=rev*10+a
        n//=10
    return rev
# Driver code
n = int(input("enter a number: "))
result = reverse(n)
print("The reverse is ", result )
