class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        s= list(s)
        i = 0
        j = len(s)-1
        while i < j:
            while s[i] not in vowels and i <len(s) -1: i += 1
            while s[j] not in vowels and j > 0: j -= 1
            if i >= j:
                break
            
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)
        
