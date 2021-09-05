"""
Problem Statement #
Implement a function rearrange(lst) which rearranges the elements such that all the negative elements appear on the left and positive elements appear at the right of the list. Note that it is not necessary to maintain the order of the input list.

Generally zero is NOT positive or negative, we will treat zero as a positive integer for this challenge! So, zero will be placed at the right.

Output #
A list with negative elements at the left and positive elements at the right

Sample Input #
[10,-1,20,4,5,-9,-6]
Sample Output #
[-1,-9,-6,10,20,4,5]

"""

def rearrange(lst):
    n = len(lst)
    l = 0
    r = n-1
    while(l<r):
        if(lst[l]>lst[r]):
            if lst[r]<0:
                lst[l],lst[r] = lst[r],lst[l]
                l = l + 1
        elif(lst[l] < lst[r]):
            if(lst[l] < 0):
                l = l + 1
                r = r - 1
            else:
                l = l + 1
    return lst


def rearrange2(lst):
    neg = list()
    pos = list()
    for x in lst:
        if(x<0):
            neg.append(x)
        else:
            pos.append(x)
    return neg + pos

#pythonic
def rearrage3(lst):
    neg = [x for x in lst if(x<0)]
    pos = [x for x in lst if(x>0)]
    return neg+pos
if(__name__ == "__main__"):
    lst = [10,-1,20,4,5,-9,-6]
    print(rearrange(lst))
    print(rearrange2(lst))
    print(rearrage3(lst))