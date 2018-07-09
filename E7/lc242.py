from collections import defaultdict

class Solution(object):
    
    def isAnagram(self, s, t):
        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counter = defaultdict(int)
        for i in range(len(s)):
            counter[s[i]] += 1
        for i in range(len(t)):
            counter[t[i]] -= 1
            
        return all( val==0 for val in counter.values())
