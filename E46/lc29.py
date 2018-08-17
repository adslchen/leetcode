class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MIN  = -2**31 
        MAX = 2**31 -1
        if dividend == MIN and divisor == MIN: return 1
        if dividend == MIN and divisor == -1: return MAX
        if dividend == 0 or divisor == MIN: return 0
        
        
        sign = -1 if (dividend < 0)^(divisor < 0) else 1
        res = 0
        divisor = abs(divisor)
        if dividend == MIN:
            dividend += divisor
            res += 1
        dividend = abs(dividend)
        
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                temp = temp << 1
                multiple = multiple << 1
            dividend -= temp
            res += multiple
            
        return res*sign
            
