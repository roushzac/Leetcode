# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if tree is empty, min depth is 0
        if root==None:
            return 0
        # if root is only node, return 0
        if root.left==None and root.right==None:
            return 1
        
        # make dictionary to keep track of minimum
        min_dict={"minimum":None}
        curr_depth=0
        
        self.DFS(root,min_dict,curr_depth)
        answer=min_dict["minimum"]
        return answer
    def DFS(self,node,dictionary,current_depth):
        current_depth+=1
        #print(node.val)
        if node==None:
            return
        if node.right==None and node.left==None:
            if dictionary['minimum']==None:
                dictionary['minimum']= current_depth
            else:
                current_min=dictionary['minimum']
                if current_min > current_depth:
                    dictionary['minimum']= current_depth
            
            return
        
        self.DFS(node.left,dictionary,current_depth)
        self.DFS(node.right,dictionary,current_depth)