class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """


        n = len(s)

        hashmap = {}
        i,j = 0, 0
        maxlen = 0

        while(i<n and j<n):
            if s[j] in hashmap:
                i = max(hashmap[s[j]]+1, i)

            hashmap[s[j]] = j
            maxlen = max(maxlen, j-i+1)
            j+=1

        return maxlen
