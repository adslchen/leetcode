class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        
        
        nums = map(int, str(num))
        last = {x:i for i, x in enumerate(nums)}
        
        for i, x in enumerate(nums):
            for j in range(9,-1,-1):
                if last.get(j) > i and j > x:
                    nums[i], nums[last[j]] = nums[last[j]], nums[i]
                    return int("".join(map(str, nums)))
        return num
        
