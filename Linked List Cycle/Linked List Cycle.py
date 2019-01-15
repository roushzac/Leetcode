# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None:
            return False
        slow=head
        fast=head
        first=True
        while slow!=None and fast!=None:
            if first==False:
                if slow==fast:
                    return True
            first=False
            slow=slow.next
            if fast.next:
                fast=fast.next.next
            else:
                fast=None
            
        return False