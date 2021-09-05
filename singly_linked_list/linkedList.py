"""
Building a linkedList class with the below methods:

The primary operations which are generally a part of the LinkedList class are listed below:

get_head() - returns the head of the list
insert_at_tail(data) - inserts an element at the end of the linked list
insert_at_head(data) - inserts an element at the start/head of the linked list
delete(data) - deletes an element with your specified value from the linked list
delete_at_head() - deletes the first element of the list
search(data) - searches for an element with the specified value in the linked list
is_empty() - returns true if the linked list is empty

"""
from Node import Node


class LinkedList(Node):
    def __init__(self):
        self.head_node = None # HeadNode is pointer to the nextnode
    
    # Time complexit is O(1) as we just getting the head
    def get_head(self):
        return self.head_node
    
    # Time complexit is O(1) as we just getting the head
    def is_empty(self):
        if(self.head_node is None):
            return True
        else:
            return False
    """
    Time complexity is O(1) as we are just doing 2 operations  
    ie: 1. Point the new node to the node which head node is pointing
        2. Point headNode to the NewNode
    """
    def insert_at_head(self,data):
        
        # Create a temp_node from the data
        temp_node = Node(data)
        # point the new node to the node which is currently pointed by headNode
        """
         head -->3-->None
                 ^
                 |
                 2
        """
        temp_node.next_element = self.head_node
        # Make headNode point to the new Node
        """
                 3-->None
                 ^
                 |
         head -->2
        
        (or)
        
        head -->2-->3-->None
        
        """
        self.head_node = temp_node
        return self.head_node
    
    # Time complexity is O(n) as we need to traverse through the list to reach the tail node
    def insert_at_tail(self,data):
        # Create a newNode with data
        newNode = Node(data)
        # check whether the list is empty, if empty call insert_at_headmenthod
        if(self.is_empty() is True):
            return self.insert_at_head(data)
        # create a temp object for the headnode's pointer
        temp = self.head_node
        # Check's whether the next node is pointing to None, if "yes" exit the loop
        while (temp.next_element is not None):
            temp = temp.next_element
        #temp will have the last node which is pointing to None
        #point the newNode to None
        # temp points to 3 and temp.next_element points to None
        
        """
         head -->3-->2-->1-->None
                              ^
                              |
                              5        
        """
        newNode.next_element = temp.next_element
        #Point the last before node to new Node
        """
        head -->3-->2-->1    None
                        |     ^
                        |     |
                        |---->5   
        (or)
        
        head -->3-->2-->1-->5-->None     
        """
        temp.next_element = newNode
        return newNode
        
            
    def print_list(self):
        temp = self.head_node
        if (self.is_empty()):
            print("LinkedList is empty")
            return False
        """
        While loop checks till the end of the linkedList
        End of linkedList will have None, so we checking till ext_element is None
        """
        print("head",end="-->")
        while(temp.next_element is not None):
            print(temp.data,end="-->")
            temp = temp.next_element # Iterator:: resetting the temp with the next node
        print(temp.data,end="--> None")
        return True
    
    # Time complexity is O(n), as we need to traverse through the whole List
    def search(self,key):
        if(self.is_empty()):
            print("LinkedList is empty")
            return False
        temp = self.head_node
        while (temp):
            if(temp.data == key):
                return temp
            temp = temp.next_element
        return False
    # Time complexity is O(1), as are deleting element at the head
    def delete_at_head(self):
        # Check wheter the list is empty, if empty dont do anything
        if(self.is_empty()):
            return self.head_node
        # Get the first_node in the linkedList
        """
         head -->3-->2-->1-->None
                     ^
                     |
            first_node(data=3,next_element=2)          
        """        
        first_node = self.head_node
        # Point headNode to firstNode's nextElement
        """
                head
                 |
                 v
                 2-->1-->None
                 ^
                 |
            first_node(data=3,next_element=2)         
        """
        self.head_node = first_node.next_element
        # Point first_node to None
        """
                head
                 |
                 v              ==> head -->2-->1-->None
                 2-->1-->None
                 
                 3-->None
                 (or)
            first_node(data=3) --> None        
        """
        first_node.next_element = None
        
        return self.head_node
    
    def get_previous_node(self,key):
        current_node = self.head_node
        if(current_node.data == key):
            return current_node
        while(current_node):
            next_node = current_node.next_element
            if(next_node != None and next_node.data == key):
                return current_node
            current_node = current_node.next_element
        return False
        
    def delete_by_value(self,key):
        if(self.is_empty()):
            print("Empty Linked List")
            return False
        previous_node = self.get_previous_node(key)
        if(previous_node):
            key_node = previous_node.next_element
            previous_node.next_element = key_node.next_element
            key_node.next_element = None
            return True
        return False
    
    def len(self):
        if(self.is_empty()):
            return 0
        temp = self.head_node
        length = 0
        while(temp):
            length = length + 1
            temp = temp.next_element
        return length
    
    # Time Complexity is O(n^2)
    def reverse(self):
        if(self.is_empty()):
            return "empty"
        temp = self.head_node
        lock = 0
        # we defined end_node as None, as before right shifting the end_node would be None
        end_node = None
        length  = self.len()-1
        #length to loop through the nodes ,if we have 4 nodes, then we need to loop through 
        # 3 times to reverse it
        while(length>0):
            while(temp.next_element is not end_node):
                # This lock is to keep a track whether the previous element is head
                if(lock == 0):
                    lock = lock + 1
                    self.head_node = temp.next_element
                # if the previous element is not head then point the previous element to next element 
                # of current node
                else:
                    previous_node.next_element = temp.next_element
                # pointing the correct nodes 
                next_node = temp.next_element
                temp.next_element = next_node.next_element
                next_node.next_element = temp
                previous_node = next_node
            # end_node is to keep a track when to stop right shifting
            end_node = temp
            # reseting the temp to point to head node's pointer
            temp = self.head_node
            # resetting the lock = 0, as we made temp to point to headnode's pointer, 
            # as temp previous element would be head
            lock = 0
            length = length - 1

        return self.head_node
    # Time complexity is O(n)
    def reverse_2(self):
        prev_node = None
        if(self.is_empty()):
            print("List is empty")
            return False
        current = self.head_node
        while(current is not None):
            next_node = current.next_element
            current.next_element = prev_node
            prev_node = current
            current = next_node
            # Setting the head value everytime 
            # so that at the end it will point to the last element in the list
            self.head_node = prev_node
        return True
            
    def reverse3(self):
          # To reverse linked, we need to keep track of three things
      previous = None # Maintain track of the previous node
      current = self.get_head() # The current node
      next = None # The next node in the list

      #Reversal
      while current:
        next = current.next_element
        current.next_element = previous
        previous = current
        current = next

        #Set the last element as the new head node
        self.head_node = previous
      return lst    
    
if(__name__=="__main__"):        
    lst = LinkedList()
    print(lst.get_head())
    print(lst.is_empty())
    lst.insert_at_head(3)
    lst.insert_at_head(2)
    lst.insert_at_head(1)
    lst.print_list()
    lst.insert_at_tail(5)
    print()
    lst.print_list()
    print()
    print(lst.search(6))
    #lst.delete_at_head()
    lst.print_list()
    print()
    #print(lst.delete_by_value(5))
    lst.print_list()
    print()
    print(lst.len())
    lst.print_list()
    print()
    #lst.reverse()
    print("-----------------------")
    #lst.reverse_2()
    #lst.printList2()
    print(lst.reverse3())
    lst.print_list()
    print()
    print(lst.reverse_2())
    lst.print_list()

    
