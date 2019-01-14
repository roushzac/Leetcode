# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root== None:
            return []
        
        level_list =[]
        curr_level = [root]
        level_list.append([root.val])
        
        while curr_level:
            next_level=[]
            next_level_vals=[]
            
            for node in curr_level:
                if node.left!=None:
                    next_level.append(node.left)
                    next_level_vals.append(node.left.val)
                    #print(node.left.val)
                if node.right!=None:
                    next_level.append(node.right)
                    next_level_vals.append(node.right.val)
                    #print(node.right.val)
            if next_level:   
                level_list.append(next_level_vals)
            curr_level = next_level
                
        return level_list
        