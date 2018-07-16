class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = [0] * 26
        for i in range(len(s)):
            dic[ord(s[i]) - ord('a')] += 1
        pos = 0 # index of the smallest s
        
        for i in range(len(s)):
            
            if ord(s[i]) < ord(s[pos]):
                pos = i
            dic[ord(s[i]) - ord('a')] -= 1
            if dic[ord(s[i]) - ord('a')] == 0:
                break
        return "" if len(s) == 0 else s[pos] + self.removeDuplicateLetters(str(s[pos+1:]).replace(s[pos],""))
