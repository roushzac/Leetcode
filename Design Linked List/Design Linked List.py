class Node:
    def __init__(self,val):
        self.val= val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length =0
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        #if inavlid index 
        if index >= self.length:
            return -1
        else:
            starting_node = self.head
            start_index =0
            
            while (starting_node.next !=None and start_index!= index):
                starting_node = starting_node.next
                start_index += 1
            return starting_node.val 
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the          insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        if self.head == None:
            self.head = Node(val)
            self.length +=1
        else:
            new_head = Node(val)
            new_head.next = self.head
            self.head = new_head
            self.length += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        starting_node = self.head
        # if its an empty linked list 
        if starting_node == None:
            self.head = Node(val)
            self.length += 1
        # otherwise 
        else:
            while starting_node.next != None:
                starting_node = starting_node.next
            new_tail = Node(val)
            starting_node.next = new_tail
            self.length += 1
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == self.length:
            self.addAtTail(val)
            
        elif index > self.length:
            return 
        else:
            index_before = index -1
            start_index =0
            starting_node = self.head
            while starting_node.next != None and start_index != index_before:
                starting_node = starting_node.next
                start_index += 1
            before = starting_node
            new_node = Node(val)
            after = before.next

            before.next = new_node
            new_node.next = after 
            self.length += 1
        
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        
        #if inavlid index 
        if index >= self.length:
            return
        # if head
        elif index ==0:
            new_head = self.head.next
            self.head = new_head
            self.length -=1
        # if tail
        elif index == self.length-1:
            new_tail_index = self.length -2
            starting_node = self.head
            start_index = 0
            while starting_node.next != None and start_index != new_tail_index:
                starting_node = starting_node.next
                start_index +=1
            starting_node.next = None
            self.length -=1
        # if middle node 
        else:
            index_before = index-1
            starting_node = self.head
            start_index = 0
            while starting_node.next != None and start_index != index_before:
                starting_node = starting_node.next
                start_index +=1
            starting_node.next = starting_node.next.next
            self.length -=1 
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)