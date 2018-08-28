class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def findNSum(nums, N, result, results, target):
            if len(nums) < N or N < 2 or nums[0]*N > target or nums[-1]*N < target:
                return
            if N == 2:
                l, r = 0, len(nums)-1
                while l<r:
                    sm = nums[l] + nums[r]
                    if sm == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]: l += 1
                    elif sm < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(0,len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                        findNSum(nums[i+1:], N-1, result+[nums[i]], results, target - nums[i])
        
        results = []
        findNSum(sorted(nums), 4, [], results, target)
        return results
