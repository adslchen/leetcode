class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        mapping = [0] * 26
        
        for i in range(len(s1)):
            mapping[ord(s1[i]) - ord('a')] += 1
            
        a = ord('a')
        dist = len(s1)
        right = 0
        left = 0
        while right < len(s2):
            if right - left  < len(s1):
                if mapping[ord(s2[right]) - a] > 0 :
                    dist -= 1
                mapping[ord(s2[right]) - a ] -= 1
                right += 1
            if right - left == len(s1) and dist == 0:
                return True
            
            if right - left == len(s1):
                if mapping[ord(s2[left]) - a] >= 0:
                    dist += 1
                mapping[ord(s2[left]) - a] += 1
                left += 1
                
        return False
