class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        sm = 0
        
        def toInt(digit):
            return ord(digit) - ord('0')
        
        m = len(num1)-1
        n = len(num2)-1
        div = 1
        while m >= 0 or n >= 0:
            if m >= 0:
                sm += toInt(num1[m])*div
            if n >= 0:
                sm += toInt(num2[n])*div
            m -= 1
            n -= 1
            div *= 10
            
        return str(sm)
