class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev = 1
        prev2 = 0
        
        for i in range(n):
            cur = prev + prev2
            prev2 = prev
            prev = cur
            
        return cur
