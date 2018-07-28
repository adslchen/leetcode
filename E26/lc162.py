class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        lo = 0
        high = len(nums)-1
        mid = 0
        
        while lo < high:
            mid = (lo + high) / 2
            if nums[mid] < nums[mid+1]:
                lo = mid + 1
            else:
                high = mid
            
        return lo
