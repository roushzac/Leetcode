# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution:
    
    
    def sortedArrayToBST(self, nums):
        def FillNode(parent, array,side):
            '''
            if side=="left":
                parent.left=TreeNode(3)
            if side=="right":
                parent.right=TreeNode(7)
            '''
            print(array)
            if array==[]:
                if side=='left':
                    #parent.left= TreeNode(None)
                    return
                if side=='right':
                    #parent.right= TreeNode(None)
                    return
            else:
                #print(array)
                mid=math.floor(len(array)/2)
                #print(mid)
                val= array[mid]
                #print(val)
                child=TreeNode(val)
                if side=="left":
                    parent.left=child
                if side=="right":
                    parent.right=child
                FillNode(child,array[0:mid],"left")
                FillNode(child,array[mid+1:len(nums)],"right")
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums==[]:
            return
        
        mid=math.floor(len(nums)/2)
        
        a= TreeNode(nums[mid])
        FillNode(a,nums[0:mid],"left")
        FillNode(a,nums[mid+1:len(nums)],"right")
        return a