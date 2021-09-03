"""
Problem Statement #
In this problem, you have to implement the findSum(lst,k) function which will take a number k as input and return two numbers that add up to k.

Input #
A list and a number k

Output #
A list with two integers a and b that add up to k

Sample Input #
lst = [1,21,3,14,5,60,7,6]
k = 81
Sample Output #
lst = [21,60]

"""

def findSum(lst,k):
    n = len(lst)
    mid = n//2
    a = lst[:mid]
    b = lst[mid:]
    for i in a:
        for j in b:
            if(i+j == k):
                return "{0} + {1} == {2}".format(i,j,k)
    return -1

def binarySearch(my_list,search):
    l = 0
    r = len(my_list)-1
    while(l<= r):
        mid = (l+r)//2
        if(my_list[mid] == search):
            return my_list[mid]
        elif(my_list[mid]<search):
            l = mid + 1
        elif(my_list[mid]>search):
            r =  mid - 1
    return -1
        
def findSum2(lst,k):
    tag = 0
    for l in lst:
        result = binarySearch(lst,k-l)
        if(result!=-1):
            print("{0} + {1} == {2}".format(l,result,k))
            tag = tag + 1
    if(tag<=0):
        print("K value not found in the list")

def findsum3(lst,k):
    left = 0
    right = len(lst)-1
    while(left!=right):
        sum = lst[left] + lst[right]
        if(sum<k):
            left = left + 1
        elif(sum>k):
            right = right - 1
        elif(sum == k):
            return (lst[left],lst[right])
    

if(__name__ == "__main__"):
    lst = [1,21,3,14,5,60,7,6]
    k = 81
    print(findSum(lst,k))
    lst.sort()
    findSum2(lst,k)
    print(findsum3(lst,k))