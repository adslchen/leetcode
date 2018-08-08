class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        hashmap = {0:-1}
        sm = 0
        for i in range(len(nums)):
            sm += nums[i]
            if k!= 0 : sm = sm % k # if k == 0, then we just need to check whether sm has appear before
            if sm in hashmap:
                if i - hashmap[sm] > 1:
                    return True
            else:
                hashmap[sm] = i
        return False
        
