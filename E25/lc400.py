class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        ln = 1
        count = 9
        start = 1
        
        while n > ln*count:
            n -= ln * count
            ln += 1
            count *= 10
            start *= 10
            
        start += (n-1) / ln
        ss = str(start)
        return int(ss[(n-1)%ln])
        
