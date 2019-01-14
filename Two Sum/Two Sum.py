class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict={}
        index=0
        for num in nums:
            num_dict[num]=index
            index+=1
        
        
        new_index=0
        for num in nums:
            complement=target-num
            if complement in num_dict:
                other_index=num_dict[complement]
                if other_index!=new_index:
                    return [new_index,other_index]
            new_index+=1