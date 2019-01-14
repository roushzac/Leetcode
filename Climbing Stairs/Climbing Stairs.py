class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        answer_dict={1:1,2:2}
        def fib(n):
            first=n-1
            second=n-2
            if n==0:
                return 0
            if n==1:
                return 1
            elif n==2:
                return 2
            elif first in answer_dict and second in answer_dict:
                answer= answer_dict[first]+ answer_dict[second]
                answer_dict[n]=answer
                return answer
            else:
                
                return fib(n-2)+fib(n-1)
            
        return fib(n)