class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0
        j = 1
        minLen = 2**31 -1
        while j <= len(nums) and i < j:
            sm = sum(nums[i:j])
            if sm >= s and (j-i) < minLen:
                minLen = j-i
            if sm < s:
                j += 1
            else:
                i += 1
        return minLen if minLen != (2**31 -1) else 0
                
