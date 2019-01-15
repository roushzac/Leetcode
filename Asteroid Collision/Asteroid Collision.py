class Stack:
    def __init__(self,List=None):
        if List==None:
            
            self.items = []
        else:
            self.items=List

    def isEmpty(self):
         return self.items == []

    def push(self, item):
         self.items.append(item)

    def pop(self):
         return self.items.pop()

    def peek(self):
        
         return self.items[len(self.items)-1]

    def size(self):
         return len(self.items)

class Solution:
    def collision(self,s1,s2):
        s1_val=abs(s1.peek())
        s2_val= abs(s2.peek())
        
        if s2_val > s1_val:
            s1.pop()
        elif s2_val < s1_val:
            s2.pop()
        elif s2_val==s1_val:
            s1.pop()
            s2.pop()
            
            
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        print("ok")
        #initialize stacks
        s1=Stack(asteroids)
        s2=Stack()
        
        
        #add everything from s1 to s2
        while s1.isEmpty()==False:
            #if s1's value is positive and s2's value is negative
            # there will be a collision
            if s2.isEmpty()==False  :
                
                if s1.peek() >=0 and s2.peek()<0 :
                    self.collision(s1,s2)
                else:
                    #print("we got here ")
                    # otherwise just add to s2
                    s2.push(s1.pop())
            else:
                
                # otherwise just add to s2
                s2.push(s1.pop())
        #add everything back to s1
        #print("exited first while loop")
        while s2.isEmpty()==False:
            s1.push(s2.pop())
            
        return s1.items