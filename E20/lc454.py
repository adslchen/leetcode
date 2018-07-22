from collections import defaultdict
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hashmap = defaultdict(int)
        
        for c in C:
            for d in D:
                sm = c+d
                hashmap[sm] += 1
        result = 0
        for a in A:
            for b in B:
                sm = a+b
                result += hashmap[-sm]
        return result
        
