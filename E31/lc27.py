class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums: return 0
        right = len(nums) -1
        
        while nums[right] == val and right >= 0:
            right -= 1
            
       
        
        for i in range(right -1, -1, -1):
            if nums[i] == val:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
        
        return right+1
