import math 
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        # get length of the array 
        length=len(nums)
        # if the list has only 1 item in it, and its not the target, the target is not in the array
        if length==1:
            if target!= nums[0]:
                true_index= -1
        # if theres nothing in the array, there is no target 
        elif length==0:
            true_index= -1
       
        mid_float=length/2
        midpoint_index= math.floor(mid_float)
        midpoint= nums[midpoint_index]
        ''' 
        start=0
        end=len(nums)
        search_done=False
        
        while search_done==False:
            midpoint=math.floor((end+start)/2)
            if (end-start)==1:
                if nums[midpoint]!=target:
                    return -1
                
            if nums[midpoint]== target:
                return midpoint
            elif nums[midpoint]== target:
                return midpoint
            elif nums[midpoint] < target:
                start= midpoint
            elif nums[midpoint] > target:
                end = midpoint
                
        return -1 
                
    
        
        
        
        
        return true_index