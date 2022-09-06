from functools import reduce

def array(list):
    list2 = []
    for i in range(len(list)):
        list2.append(list[i][1])
    arr = reduce(lambda a,b : a+b,list2)
    if arr == 0:
        return True
    
    return False


list = [[1,0,3],[3,0,5],[1,0,3],[3,0,5]]
if array(list):
    print('invalid data')
else:
    print("valid data")

    