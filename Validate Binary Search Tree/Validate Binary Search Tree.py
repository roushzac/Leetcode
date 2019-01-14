# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution:
    def isValidBST(self, root, minimum=-math.inf, maximum=math.inf):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # if its empty, its a valid BST
        if root==None:
            return True
        
        
        rootval=root.val
        leftvalid=False
        rightValid=False
        
        # if left node i None, thats ok
        if root.left == None:
            leftvalid=True
        # if left is a real node, we need to make sure its les than the root
        else:
            # if its less than the root, the left node i valid
            if root.left.val < rootval and self.InRange(minimum,maximum,root.left.val)==True:
                leftvalid=True
            # if its greater, its not valid 
            else:
                leftvalid=False
        
        # if right node i None, thats ok
        if root.right == None:
            rightvalid=True
        # if right is a real node, we need to make sure its greater than the root
        else:
            # if its less than the root, the left node i valid
            if root.right.val > rootval and self.InRange(minimum,maximum,root.right.val)==True:
                rightvalid=True
            # if its greater, its not valid 
            else:
                rightvalid=False
        rootIsValid= rightvalid and leftvalid 
        
        
        
        
        left=self.isValidBST( root.left,minimum,rootval)
        right= self.isValidBST(root.right,rootval,maximum)
        
        return rootIsValid and left and right 
    
    
    def InRange(self,mini,maxi,val):
        if val < maxi and val > mini :
            return True
        else:
            return False