"""
Problem Statement #
Implement a function findSecondMaximum(lst) which returns the second largest element in the list.

Input: #
A List

Output: #
Second largest element in the list

Sample Input #
[9,2,3,6]
Sample Output #
6

"""

def findSecondMaximum(lst):
    i = 0
    j = 0
    n = len(lst)
    myList = [0]*(n)
    while(i<n and j<n):
        if(lst[i]>myList[j]):
            myList[j] = lst[i]
            i = i + 1
        elif(lst[i]<myList[j]):
            temp = myList[j]
            myList[j] = lst[i]
            myList[j+1] = temp
            j = j + 1
            i = i + 1
    if(len(myList)>=2):
        return myList[-2]
    else:
        return -1
    
def findSecondMaximum2(lst):
    max = -1
    secMax = -1
    for i in range(len(lst)):
        if(lst[i]>max):
            t = max
            max =  lst[i]
            if(secMax<t):
                secMax = t
        elif(lst[i]>secMax):
            secMax = lst[i]
    return secMax

if(__name__=="__main__"):
    lst = [9,2,3,6]
    lst1 = [5,1,2,0,4]
    print(findSecondMaximum(lst))
    print(findSecondMaximum(lst1))
    print(findSecondMaximum2(lst))
    print(findSecondMaximum2(lst1))