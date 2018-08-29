class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0],nums[1])
        dp = [0] * (len(nums)+1)
        dp[1] = nums[0]
        dp[2] = nums[1]
        for i in range(2,len(nums)):
            dp[i+1] = max(dp[i-1], dp[i-2]) + nums[i]
        
        #print(dp)
        return max(dp[-1], dp[-2])
