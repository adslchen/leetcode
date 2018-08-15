class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        N = len(nums)
        dp = [[] for _ in xrange(N)]
        ans = []
    
        for i in xrange(N-2,-1,-1):
            ni = nums[i]
            seen = set()
            for j in xrange(i+1, N):
                nj = nums[j]
                if ni <= nj and nj not in seen:
                    seen.add(nj)
                    dp[i].extend([[ni] + x for x in [[nj]] + dp[j]])
                
        seen = set()
        for i in xrange(N):
            if nums[i] not in seen:
                seen.add(nums[i])
                ans += dp[i]
        return ans
