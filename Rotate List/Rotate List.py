# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return
    
        loop=head
        c=1
        while loop.next!=None:
            loop=loop.next
            c=c+1
        loop.next=head
        k=k%c
        k=c-k
        while k>0:
            head=head.next
            loop=loop.next
            k-=1
        loop.next=None
        return head