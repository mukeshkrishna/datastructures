class myStack():
    def __init__(self):
        self.stackList = []
    
    def isEmpty(self):
        return len(self.stackList) == 0
    
    def top(self):
        if(self.isEmpty()):
            return None
        return self.stackList[-1]
    
    def push(self,value):
        self.stackList.append(value)

    def pop(self):
        if(self.isEmpty()):
            return None
        return self.stackList.pop() 
    
    def size(self):
        return len(self.stackList)

    def getStack(self):
        return self.stackList

if(__name__ == "__main__"):
    stack = myStack()
    for i in range(5):
        stack.push(i)
    print(stack.top())
    print(stack.getStack())
    print(stack.pop())
    print(stack.pop())
    print(stack.getStack())
    
