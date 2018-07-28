class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [None] * n
        for s in range(n-1,-1,-1):
            dp[s] = nums[s]
            for e in range(s+1, n):
                dp[e] = max(nums[s] - dp[e],nums[e] - dp[e-1])
                
        return dp[n-1] >= 0
                
