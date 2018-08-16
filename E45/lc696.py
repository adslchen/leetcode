class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isBinSub(s, x, y):
            count = 1
            while x > 0 and y < len(s)-1 and s[x] == s[x-1] and s[y] == s[y+1]:
                x -= 1
                y += 1
                count += 1
            return count
            
        ans = 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                ans += isBinSub(s, i-1, i)
                
        return ans
