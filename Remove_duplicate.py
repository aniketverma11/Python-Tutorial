def func(l):
    a = []
    for i in l:
        if i not in a:
            a.append(i)
    return a


l = input('Enter list: ')
arr = list(func(l))
for i in range (0, len(arr)):
    arr[i] = int(arr[i])
print(arr)









"""arr = [2,2,5,5,6,6,4,4,8,8,7,7,9,9]
print('Intial list: ', arr)
#first set func converts the list into set
#and it removes duplicate and sort the list too.
b = set(arr)
#convert back modified set into list 
print('Modified List: ',list(b))"""

