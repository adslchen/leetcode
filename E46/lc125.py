class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        
        i = 0
        j = len(s)-1
        while i < j:
            while i < len(s) and s[i] not in alpha:
                i += 1
            while j > 0 and s[j] not in alpha:
                j -= 1
                
            if i < j and s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
