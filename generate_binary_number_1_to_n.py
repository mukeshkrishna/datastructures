from Queue import myQueue

class mybinaryConversion(myQueue):
    
    def binaryConversion(self,value):
        binary_converted = str()
        while(True):
            rem = value%2
            ques = value//2
            binary_converted = binary_converted + str(rem)
            if(ques == 0):
                break
            value = ques
        return binary_converted
            
    


if(__name__=="__main__"):
    
    binary = mybinaryConversion()
    queue = myQueue()
    n = 3
    for i in range(1,n+1):
        queue.enqueue(binary.binaryConversion(i))
    print(queue.getQueue())