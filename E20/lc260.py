class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = 0
        
        for n in nums:
            diff ^= n
        
        diff &= -diff
        
        ret = [0, 0]
        for n in nums:
            if n & diff == 0: # last bit is not set
                ret[0] ^= n
            if n & diff != 0: # last bit set
                ret[1] ^= n
        return ret
        
