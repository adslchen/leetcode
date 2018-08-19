class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        dp = [0]*len(nums)
        
        maxsum = nums[0]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            maxsum = max(dp[i], maxsum)
            
        return maxsum"""
        
        return self.helper(nums, 0, len(nums)-1)
    
    
    def helper(self, nums, L, R):
        
        if L > R:
            return -2**31
        M = (L+R) / 2
        
        leftans = self.helper(nums, L, M-1)
        rightans = self.helper(nums, M+1, R)
        
        leftmax = 0
        sm = 0
        for i in range(M-1, L-1, -1):
            sm += nums[i]
            leftmax = max(sm, leftmax)
            
        rightmax = 0
        sm = 0
        for i in range(M+1, R+1):
            sm += nums[i]
            rightmax = max(sm, rightmax)
            
        return max(leftmax + nums[M] + rightmax, leftans, rightans)
