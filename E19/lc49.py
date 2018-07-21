class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapping = {}
        for i in range(len(strs)):
            stringKey = [0]*26
            for j in range(len(strs[i])):
                stringKey[ord(strs[i][j]) - ord('a')] += 1
            if tuple(stringKey) not in mapping:
                mapping[tuple(stringKey)] = [strs[i]]
            else:
                mapping[tuple(stringKey)].append(strs[i])
        result = [ value for key, value in mapping.items()]
        return  result
        
