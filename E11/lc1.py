class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        hashmap = {}
        for i in range(n):
            key = target - nums[i]
            if nums[i] in hashmap:
                return hashmap[nums[i]], i
            hashmap[key] = i
            
