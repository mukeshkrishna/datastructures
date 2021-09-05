"""
Input: #
A sorted list

Output: #
A list with elements stored in max/min form

Sample Input #
lst = [1,2,3,4,5]
Sample Output #
lst = [5,1,4,2,3]

"""
def maxMin(lst):
    newList = list()
    n = len(lst)
    left = 0
    right = n - 1
    if(len(lst) == 0):
        return []
    while(left<=right):
            if(left == right):
                newList.append(lst[left])
                left = left + 1
            else:
                newList.append(lst[right])
                newList.append(lst[left])
                left = left + 1
                right = right - 1
    return newList
    
if(__name__ == "__main__"):
    lst = [1,2,3,4,5]
    print(maxMin(lst))