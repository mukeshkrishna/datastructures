from Node import Node

class LinkedList(Node):
    def __init__(self):
        self.head = None
            
    def isEmpty(self):
        if(self.head == None):
            return True
        else:
            return False
    def get_head(self):
        return self.head
    
    def insert_at_head(self,data):
        new_node = Node(data)
        temp = self.head
        if(self.isEmpty()):
            new_node.next_element = self.head
            self.head = new_node
            new_node.previous_element = None
            return True
        
        next_node = self.head
        new_node.next_element = self.head
        self.head = new_node
        new_node.previous_element = None
        next_node.previous_element = new_node
        
        
        
    def print_list(self):
        if(self.isEmpty()):
            print("head-->None")
            return True 
        temp = self.head
        print("head",end="-->")
        while(temp.next_element is not None):
            print(temp.data,end="-->")
            temp = temp.next_element
        print(temp.data,end="-->None")
        return True
    
    def delete(self,key):
        if(self.isEmpty()):
            return False
        temp = self.head
        while(temp):
            if(temp.data == key):
                key_node = temp
                key_nodes_next = key_node.next_element
                key_nodes_previous = key_node.previous_element
                
                key_nodes_previous.next_element = key_nodes_next
                key_nodes_next.previous_element = key_node.previous_element
                
                key_node.previous_element = None
                key_node.next_element = None
                return True
            temp = temp.next_element
        return False
    
    def len(self):
        if(self.isEmpty()):
            return 0
        temp = self.head
        length = 0
        while(temp):
            length = length+1
            temp = temp.next_element
            
        return length
                            
        
            
if(__name__ == "__main__"):
    lst = LinkedList()
    lst.insert_at_head(4)
    lst.insert_at_head(3)
    lst.insert_at_head(2)
    lst.insert_at_head(1)
    
    lst.print_list()
    print()
    print(lst.len())
    lst.delete(3)
    lst.print_list()
    print()
    print(lst.len())