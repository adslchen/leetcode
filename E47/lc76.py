from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = Counter(t)
        missing = len(t)
        
        start =0
        end = 0
        i = 0
        
        for j, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            
            if missing == 0:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if end == 0 or j - i < end - start:
                    start, end  = i, j
                    
                need[s[i]] += 1
                missing += 1
                i += 1
                
        return s[start:end]
