class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        Len = len(s)
        for i in range(Len):
            ret = ret * 26 + (ord(s[i])-64)
        return ret
