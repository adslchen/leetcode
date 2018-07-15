class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        
        while n > 1:
            res = n%3
            if res != 0:
                return False
            n /= 3
        return True
        
