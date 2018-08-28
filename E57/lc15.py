class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ans = []
        prev = None
        for i in range(len(nums)-2):
            if nums[i] == prev:
                continue
            pivot = nums[i]
            target = -pivot
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    ans.append([pivot, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < len(nums) and nums[left] == nums[left-1]: left += 1
                    while right > pivot and nums[right] == nums[right+1]: right -= 1
            prev = nums[i]
        return ans
