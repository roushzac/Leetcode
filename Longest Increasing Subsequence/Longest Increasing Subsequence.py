class Solution:
    
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        best =[]
        for i in range(len(nums)):
            best.append(1)
        
        for i in range(len(nums)):
            for j in range(0,i):
                ival = nums[i]
                jval = nums[j]
                
                if ival > jval and best[j] >= best[i]:
                    best[i] =best[j] + 1
         
        print(best)
        return max(best)