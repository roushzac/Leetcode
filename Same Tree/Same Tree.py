# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        def GetTreeList(TreeList,node):
            if node==None:
                TreeList.append(None)
                return
            TreeList.append(node.val)
            GetTreeList(TreeList,node.left)
            GetTreeList(TreeList,node.right)
            
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        p_list=[]
        q_list=[]
        
        GetTreeList(p_list,p)
        GetTreeList(q_list,q)
        
        if p_list==q_list:
            return True
        else:
            return False