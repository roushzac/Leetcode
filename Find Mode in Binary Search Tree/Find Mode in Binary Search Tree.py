# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def BFS(node,mode_dict, tree_dict):
            if node==None:
                return
            
            
            value= node.val
            #print(value)
            # if weve seen the value before, increment its count
            if value in tree_dict:
                tree_dict[value]+=1
            # otherwise set its count to 1
            else:
                tree_dict[value]=1
            # if the value is the mode, increment its count
            #
            if value in mode_dict['mode'][1]:
                mode_dict["mode"][0]+=1
                mode_dict["mode"][1]=[value]
                
            # if the node frequency is greater than the mode frequency, replace the mode 
            if tree_dict[value] > mode_dict["mode"][0]:
                mode_dict["mode"] = [tree_dict[value],[value]]
            
            # if node frequency == mode frequency , add to list of mode nodes 
            if tree_dict[value]== mode_dict["mode"][0]:
                mode_dict["mode"][1].append(value)
                
                
            BFS(node.left,mode_dict,tree_dict)
            BFS(node.right,mode_dict,tree_dict)
        # initialize dictionary for the mode and dictionary for all te nodes of the tree
        
        if root==None:
            return []
        root_val= root.val
        mode_dict={}
        mode_dict["mode"]=[1,[root_val]]
        tree_dict={}
        tree_dict[root_val]=1
        
        # breadth first search the entire tree, find mode
        BFS(root.left,mode_dict, tree_dict)
        BFS(root.right,mode_dict, tree_dict)
        
        answer= set(mode_dict["mode"][1])
        print(answer)
        answer2=[]
        for a in answer:
            #b=TreeNode(a)
            answer2.append(a)
        
        return answer2