# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        prev = None
        curr = head 
        n = curr.next
        
        while n!= None:
            curr.next = prev
            prev = curr
            curr = n
            n = n.next
        curr.next = prev
        head = curr
        return head 
        