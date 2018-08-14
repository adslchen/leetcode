class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in range(len(s)):
            ans += self.isPalin(s, i, i)
            ans += self.isPalin(s, i, i+1)
        return ans
        
        
    def isPalin(self, s, i, j):
        res = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            res += 1
            i -= 1
            j += 1
        return res
