class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        sm = sum(nums)
        if sm % 2 == 1:
            return False
        target = sm / 2
        dp = [False] * sm
        
        dp[0] = True
        for i in range(len(nums)):
            for j in range(sm-1, -1, -1):
                if j >= nums[i]:
                    dp[j] = dp[j] or dp[j-nums[i]]
                    
        return dp[target]
