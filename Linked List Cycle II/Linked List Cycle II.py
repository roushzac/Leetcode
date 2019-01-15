# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None
        Node_table={}
        slow=head
        fast=head
        first=True
        #Node_table[head]=1
        
        while slow!=None and fast!=None:
            """
            if first==False:
                if slow==fast:
                    return slow
            first=False
            """
            if slow in Node_table:
                Node_table[slow]+=1
                #print(Node_table)
                return slow
            else:
                Node_table[slow]=1
            slow=slow.next
            if fast.next:
                fast=fast.next.next
            else:
                fast=None
        
        
        return None