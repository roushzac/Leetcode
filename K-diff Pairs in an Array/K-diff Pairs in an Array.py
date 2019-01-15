class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        nums.sort()
        present_dict={}
        for num in nums:
            if num not in present_dict:
                present_dict[num]=1
            else:
                present_dict[num]+=1 
        kpairs=set()
        for num in nums:
            kplus= num+ k
            kminus= num-k
            if k ==0:
                if present_dict[num] > 1:
                    kpairs.add((num,num))
            else:
                if kplus in present_dict:
                    kpairs.add((num,kplus))
                
        print(kpairs)
        return len(kpairs)