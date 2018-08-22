class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cumsum = [0]*(len(nums)+1)
        posLeft = [0]*(len(nums))
        posRight = [0] *(len(nums))
        ans = [-1,-1,-1]
        n = len(nums)
        for i in range(len(nums)):
            cumsum[i+1]  = nums[i] + cumsum[i]
        # find posLeft
        tot = cumsum[k] - cumsum[0]
        for i in range(k, n):
            if cumsum[i+1] - cumsum[i-k+1] > tot:
                posLeft[i] = i-k+1
                tot = cumsum[i+1] - cumsum[i-k+1]
            else:
                posLeft[i] = posLeft[i-1]
        # find posRight
        tot = cumsum[n] - cumsum[n-k]
        posRight[n-k] = n-k
        for i in range(n-k-1, -1, -1):
            if cumsum[i+k] - cumsum[i] >= tot:
                tot = cumsum[i+k] - cumsum[i]
                posRight[i] = i
            else:
                posRight[i] = posRight[i+1]
        #print(posLeft)
        
        #print(posRight)
        # find all middle interval
        maxsm = 0
        for i in range(k,n-2*k+1):
            l = posLeft[i-1]
            r = posRight[i+k]
            sm = (cumsum[i+k] - cumsum[i]) + (cumsum[l+k] - cumsum[l]) + (cumsum[r+k] - cumsum[r])
            if sm > maxsm:
                maxsm = sm
                ans[0] = l
                ans[1] = i
                ans[2] = r
        return ans
