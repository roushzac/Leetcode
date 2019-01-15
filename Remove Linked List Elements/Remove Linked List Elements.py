# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head==None:
            return None
        if head.val==val:
            head=self.NextValidNode(head,val)
        currNode=head
        while currNode!=None:
            #print(currNode.val)
            if currNode.next:
                if currNode.next.val == val:
                    currNode.next= self.NextValidNode(currNode.next,val)
            currNode=currNode.next
            
        return head
        
    def NextValidNode(self,node,badval):
        #print(node.val)
        if node.val!= badval:
            #print(node.val)
            return node
        while node.next!=None:
            if node.next.val!=badval:
                #print(node.val)
                return node.next
            node=node.next
            print(node.val)
        return None
            