class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        if len(p) > len(s):
            return []
        result = []
        d1 = [0]*26
        d2 = [0]*26
        window = len(p)
        for i in range(window):
            d1[ord(p[i]) - ord('a')] += 1
            d2[ord(s[i]) - ord('a')] += 1
            
        if self.counter(d1, d2):
            result.append(0)
        
        start = 0
        end = window
        while end < len(s):
            d2[ord(s[start]) - ord('a')] -= 1
            d2[ord(s[end]) - ord('a')] += 1
            if self.counter(d1, d2):
                result.append(start+1)
            start += 1
            end += 1
            
            
        return result
            
    def counter(self, d1, d2):
        d = [a - b for a, b in zip(d1,d2)]
        for a in d:
            if a != 0:
                return False
        return True
