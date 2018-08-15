class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0 
        j = len(s)-1
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
            
        return self.isPal(s, i+1, j) or self.isPal(s, i, j-1)
        
        
        
    def isPal(self, s, start, end):
        n = (end-start+1) / 2
        for i in range(n):
            if s[start+i] != s[end-i]:
                return False
        return True
        
