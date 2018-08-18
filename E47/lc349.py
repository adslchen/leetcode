class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = set()
        hashmap = set()
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        for item in nums1:
            hashmap.add(item)
            
        for item in nums2:
            if item in hashmap:
                ans.add(item)
                
        return list(ans)
            
