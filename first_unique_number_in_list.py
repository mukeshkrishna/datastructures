"""
Problem Statement #
Implement a function, findFirstUnique(lst) that returns the first unique integer in the list.

Input #
A list of integers

Output #
The first unique element in the list

Sample Input #
[9,2,3,2,6,6]
Sample Output #
9
"""

def findFirstUnique(lst):
    myList = list()
    for x in lst:
        if x not in myList:
            myList.append(x)
        else:
            myList.remove(x)
    return myList[0]

if(__name__=="__main__"):
    lst = [9,2,3,2,6,6]
    lst2 = [4,5,1,2,0,4]
    print(findFirstUnique(lst))
    print(findFirstUnique(lst2))