class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        lastfoundnotzero = 0
        for i in range(n):
            if nums[i] != 0:
                nums[lastfoundnotzero] = nums[i]
                lastfoundnotzero += 1
        for i in range(lastfoundnotzero,n):
            nums[i] = 0
