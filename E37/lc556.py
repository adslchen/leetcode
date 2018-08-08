class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = list(str(n))
        nums = map(int, nums)
        
        # first find the start decreasing element
        pivot = len(nums) - 1
        for i in range(len(nums) -2 ,-1 ,-1):
            if nums[i] < nums[i+1]:
                break
            pivot = i
​
            
        
        if pivot == 0: # pivot == 0 means every element is incresing e.g. 54321
            return -1
        pivot = pivot-1
     
        sw = pivot
        for i in range(pivot+1, len(nums)):
            if nums[i] > nums[pivot]:
                sw = i
        
        nums[pivot], nums[sw] = nums[sw], nums[pivot]
       
        # flip the numbers right to the pivot
    
        def reverse(array, start, end):
            m = (end - start +1) / 2
            
            for i in range(m):
                array[i+start], array[end - i] = array[end-i], array[i+start]
        
        
        reverse(nums, pivot+1, len(nums)-1)
        ret = 0
        for i in range(len(nums)):
            if ret >= (2**31 - 1) / 10:
                if ret == (2**31 - 1) / 10 and nums[i] >= 8:
                    return -1
                elif ret > (2**31 - 1)/ 10:
                    return -1
                    
            ret = ret * 10 + nums[i]
            
        return ret
