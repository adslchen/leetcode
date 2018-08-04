class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        mindist = 2**31 -1 
        mintar = 0
        for p in range(len(nums)-2):
            pivot = nums[p]
            tar = target - pivot
            i = p+1
            j = len(nums) - 1
            while i < j:
                sm = nums[i] + nums[j]
                if abs(tar - sm) < mindist:
                    mindist = abs(tar -sm)
                    mintar = sm + pivot
                if sm < tar:
                    i += 1
                elif sm > tar:
                    j -= 1
                else:
                    return target
        return mintar
                    
