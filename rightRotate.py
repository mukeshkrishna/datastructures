"""
Problem Statement #
Implement a function rightRotate(lst,n) which will rotate the given list by k. This means that the right-most elements will appear at the left-most position in the list and so on. You only have to rotate the list by one element at a time.

Input #
A list and a number by which to rotate that list

Output: #
The given list rotated by k elements

Sample Input #
lst = [10,20,30,40,50]
n = 3
Sample Output #
lst = [30,40,50,10,20]

"""

def rightRotate(lst,n):
    i = 0
    count = 0
    while(count<n-1):
        temp = lst[i]
        lst.pop(i)
        lst.append(temp)
        count = count + 1
    return lst

#Pythonic rotation based out of slicing
def rightRotate2(lst,n):
    return lst[n-1:] + lst[:n-1]

if(__name__ == "__main__"):
    lst = [10,20,30,40,50]
    n = 3
    print(rightRotate(lst,n))
    print(rightRotate2(lst,n))