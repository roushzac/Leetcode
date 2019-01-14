# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def Recursion(root,List=[]):
            print("in recursion")
            print(List)
            if root==None:
                return []

            Recursion(root.left,List)
            rootval=root.val

            List.append(rootval)
            Recursion(root.right,List)

            return List
        return Recursion(root,List=[])