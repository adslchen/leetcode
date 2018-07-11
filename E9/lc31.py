class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if not nums or len(nums) == 1:
             return 
        
        n = len(nums)
        # find the first decending digit(pivot)
        pivot = 0
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        print(pivot)
        if nums[pivot] < nums[pivot+1]:
        
            # find the smalles digit to the right of pivot which > digit. swap pivot and digit
            least = 0
            for i in range(pivot+1,n):
                if nums[i] > nums[pivot]:
                    least = i
            nums[pivot], nums[least] = nums[least], nums[pivot]
            
        
        # reverse the digits to the right of pivot
            x = (n -pivot -1)/2
            for i in range(x):
                nums[pivot+i+1], nums[n-i-1] = nums[n-i-1], nums[pivot+i+1]
            
        else:
            x = (n-pivot) /2
           
            for i in range(x):
                nums[i], nums[n-i-1] = nums[n-i-1], nums[i]
