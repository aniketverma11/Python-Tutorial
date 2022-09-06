def palindrome(n):
    rev = 0
    x = n
    while n>0:
        a = n%10
        rev = rev*10+a
        n//=10
    if x==rev:
        print("Number is Palindrom: ")
        return rev
    else:
        print("Number is not palindrom: ")

n = int(input("Enter a number"))    
print ("The palindrome is: ", palindrome(n))

