class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        A = set(nums)
        n = len(nums)
        disapperNums = []
        for i in range(1,n+1):
            if i not in A:
                disapperNums.append(i)
        return disapperNums
        
