"""
Problem Statement #
Implement a function, findProduct(lst), which modifies a list so that each index has a product of all the numbers present in the list except the number stored at that index.

Input: #
A list of numbers (could be floating points or integers)

Output: #
A list such that each index has a product of all the numbers in the list except the number stored at that index.

Sample Input #
arr = [1,2,3,4]
Sample Output #
arr = [24,12,8,6]

"""

def mult(a):
    prod = 1
    for x in a:
        prod = prod * x
    return prod

def findProduct(arr):
    myList = list()
    n =  len(arr)
    for index,value in enumerate(arr):
        if(index < n-1):
            myList.append(mult(arr[:index])*mult(arr[index+1:]))
        else:
            myList.append(mult(arr[:index]))
    return myList

def findProduct2(arr):
    myList = list()
    leftProduct = 1
    for index,val in enumerate(arr):
        rightProduct = mult(arr[index+1:])
        myList.append(leftProduct*rightProduct)
        leftProduct = leftProduct * arr[index]
    return myList
    
def findProduct3(lst):
    # get product start from left
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele
    # get product starting from right
    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]

    return product
if(__name__ == "__main__"):
    arr = [1,2,3,4]
    arr1 = [4,2,1,5,0]
    print(findProduct(arr))
    print(findProduct(arr1))
    print(findProduct2(arr))
    print(findProduct2(arr1))
    print(findProduct3(arr))
    print(findProduct3(arr1))