class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        index=0
        length= len(nums)
        second_index=index+1
        while index < length-1:
            
            
            
            num1=nums[index]
            num2=nums[second_index]
            #print(str(num1)+" "+str(num2))
            #print("index= "+str(index)+" second index= "+str(second_index))
            
            while num1==num2:
                del nums[second_index]
                length-=1
                if index!= length-1:
                    num1=nums[index]
                    num2=nums[second_index]
                else: 
                    break
            
            second_index+=1
            index+=1
            
        return length
        