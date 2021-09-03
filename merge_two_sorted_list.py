"""Problem Statement #
Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list. Name it merge_lists(lst1, lst2).

Input #
Two sorted lists.

Output #
A merged and sorted list consisting of all elements of both input lists.

Sample Input #
list1 = [1,3,4,5]  
list2 = [2,6,7,8]
Sample Output #
arr = [1,2,3,4,5,6,7,8]

"""

def merge_lists(list1,list2):
    i = 0 
    j = 0
    n = len(list1)
    m = len(list2)
    tempList = list()
    while(i<n or j<m):
        if i == n :
            tempList.append(list2[j])
            j = j + 1
        elif j == m :
            tempList.append(list1[i])
            i =  i + 1
        elif(list1[i]<list2[j]):
            tempList.append(list1[i])
            i = i + 1
        elif(list2[j]<list1[i]):
            tempList.append(list2[j])
            j = j + 1 
        else:
            tempList.append(list1[i]) 
            i =  i + 1
            j = j + 1  
    return tempList    

def merge_lists2(list1,list2):
    i = 0 
    j = 0
    n = len(list1)
    m = len(list2)
    tempList = list()
    while(i<n and j<m):
        if(list1[i]<list2[j]):
            tempList.append(list1[i])
            i = i + 1
        elif(list2[j]<list1[i]):
            tempList.append(list2[j])
            j = j + 1 
    if(i<n):
        tempList.extend(list1[i:])
    elif(j<m):
        tempList.extend(list2[j:])
        
    return tempList 
    
def merge_lists3(list1,list2):
    list1.extend(list2)
    print(list1)    
    
if(__name__ == "__main__"):
    list1 = [1,3,4,5]  
    list2 = [2,6,7,8]
    print(merge_lists(list1,list2))
    print(merge_lists2(list1,list2))
    merge_lists3(list1,list2)
