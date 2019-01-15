# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import math
class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        even = False
        
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        # if its even 
        if fast.next!= None:
            return slow.next
        return slow
            