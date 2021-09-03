"""
Problem Statement #
Implement a function findMinimum(lst) which finds the smallest number in the given list.

Input: #
A list of integers

Output: #
The smallest number in the list

Sample Input #
arr = [9,2,3,6]
Sample Output #
2

"""

def findMinimum(arr):
    small = arr[0]
    if len(arr) == 0:
        return -1
    for x in arr:
        if(small>x):
            small = x
    return small

if(__name__=="__main__"):
    arr = [9,2,3,6]
    arr1 = [4,2,1,5,0]
    print(findMinimum(arr))
    print(findMinimum(arr1))