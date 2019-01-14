# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, summ):
        def FindPath(parent,summ,currsum):
            if parent==None:
                return
            else:
                currsum+=parent.val
            if parent.left==None and parent.right==None:
                print("leaf= "+str(parent.val)+" value of cursum= "+str(currsum))
                
                
                if currsum==summ:
                    return True
                else:
                    return False
                
            else:
                left= FindPath(parent.left,summ,currsum)
                right= FindPath(parent.right,summ,currsum)
                if left== True or right == True:
                    return True
                else:
                    return False
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root==None:
            return False
        if root.val== summ and root.left==None and root.right==None:
            return True
        answer= False
        currsum=0
        left=FindPath(root,summ,currsum)
        right= FindPath(root,summ,currsum)
        
        if left== True or right == True:
            return True
        else:
            return False