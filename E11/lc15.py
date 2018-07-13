class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        n = len(nums)
        ans = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -(nums[i])
            if target < 0 :
                break
            j = i+1
            k = n-1
            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] +  nums[k] < target:
                    j += 1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < n-1 and nums[j] == nums[j-1]: j += 1
                    while k > i+1 and nums[k] == nums[k+1]: k -= 1
                    
        return ans
