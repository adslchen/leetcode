class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dictionary = [0]* 26
        
        a =  ord('a')
        
        for i in range(len(s)):
            dictionary[ord(s[i]) - a] += 1
        
        for i in range(len(t)):
            dictionary[ord(t[i]) - a] -= 1
            if dictionary[ord(t[i]) - a] < 0:
                return t[i]
            
        return ""
        
