class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.min=None
        self.length=0
        self.min_stack=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        
        if self.min==None:
            self.min=x
            
            self.min_stack.append(x)
            
        else:
            
            if self.min > x:
                #print(x)
                self.min=x
                ###
                self.min_stack.append(x)
            else:   
                self.min_stack.append(self.min)
            
        self.stack.append(x)
        self.length+=1

    def pop(self):
        """
        :rtype: void
        """
        item=self.stack.pop()
        self.length-=1
        if item == self.min:
            
            self.min_stack.pop()
            if len(self.min_stack)!=0:
                self.min=self.min_stack[len(self.min_stack)-1]
                
            else:
                self.min=None
        else:
            self.min_stack.pop()
          
        return item
        

    def top(self):
        """
        :rtype: int
        """
        item=self.stack[self.length-1]
        return item

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()