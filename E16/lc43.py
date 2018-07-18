class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        pos = [0] * (m+n)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                a = ord(num1[i]) - ord('0')
                b = ord(num2[j]) - ord('0')
                p1 = i+j
                p2 = i+j+1
                sm = pos[p2] + a*b
                pos[p2] = sm % 10
                pos[p1] += sm / 10
        result = ""    
        for p in pos:
            if p ==0 and result == "":
                continue
            result += str(p)
        return "0" if result == "" else result
        
