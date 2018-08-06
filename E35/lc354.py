import functools
import bisect
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def compare(item1, item2):
            if item1[0] == item2[0]:
                return item2[1] - item1[1]
            else:
                return item1[0] - item2[0]
        envelopes = sorted(envelopes, key=functools.cmp_to_key(compare))
        
        dp = [0] * len(envelopes)
        ln = 0
        for env in envelopes:
            index = bisect.bisect_left(dp, env[1], 0, ln)
            if index < 0:
                index = -(index + 1)
            dp[index] = env[1]
            if index == ln:
                ln += 1
        
        return ln
