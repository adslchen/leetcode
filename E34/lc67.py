class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = len(a)
        m = len(b)
        digit = 1
        ans = []
        sm = 0
        while n-digit >= 0 or m-digit >=0:
            
            if n-digit >= 0:
                sm += int(a[n-digit])
            if m-digit >= 0 :
                sm += int(b[m-digit])
            ans.append(str(sm%2))
            sm /= 2
            digit += 1
        if sm >= 1:
            ans.append(str(sm))
        
        
        return "".join(ans[::-1])
            
