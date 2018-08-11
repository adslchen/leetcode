class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashMap = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in hashMap:
                return True
            hashMap[nums[i]] = i
        
        return False
