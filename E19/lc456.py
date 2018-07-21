class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        
        if len(nums) < 3:
            return False
        stack = []
        Min = [0]* len(nums)
        Min[0] = nums[0]
        for i in range(1,len(nums)):
            Min[i] = min(nums[i], Min[i-1])
        for j in range(len(nums)-1, -1, -1):
            if nums[j] > Min[j]:
                while stack and stack[-1] <= Min[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        return False
