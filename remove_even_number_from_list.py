"""
Problem Statement #
Implement a function which removes all the even elements from a given list. Name it removeEven(list).

Input #
A list with random integers.

Output #
A list with only odd integers

Sample Input #
myList = [1,2,4,5,10,6,3]
Sample Output #
myList = [1,5,3]

"""
myList = [1,2,4,5,10,6,3]
def removeEven(myList):
    tempList = list()
    for index,value in enumerate(myList):
        if(value % 2 != 0):
            tempList.append(value)
    return tempList
            
def removeEven2(myList):
    print([ x for x in myList if x%2 != 0])

def removeEven3(myList):
    i = 0
    n = len(myList)
    tempList = list()
    while(i<n):
        if(myList[i]%2 != 0):
            tempList.append(myList[i])
        i = i + 1
    return tempList
    
if(__name__ == "__main__"):
    print(removeEven(myList))
    removeEven2(myList)
    print(removeEven3(myList))