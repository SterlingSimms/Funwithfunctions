def oddEven():
    for count in range(1, 2001):
        if count % 2 == 0:
            a = "This is an even number!"
        if count % 2 == 1:
            a = "This is an odd number!"
        print count, a
oddEven()

def multiply(list, xmultiply):
    newList = []
    for value in list:
        newList.append(value * xmultiply)
    return newList
multiply([1,2,3,4,5], 5)


def layeredMultiples(arr):
    ans = []
    for value in arr:
        newList = []
        for x in range(0, value):
            newList.append(1)
        ans.append(newList)
    return ans
print layeredMultiples(multiply([1,2,3,4,5], 5))






    

    