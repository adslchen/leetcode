# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 100
        right = n
        left = 1
        while left < right:
            M = (right+left)/2
            res = guess(M)
            if res == 1:
                left = M+1
            elif res == -1:
                right = M
            else: 
                return M
        return left
                
