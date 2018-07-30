import sys
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        def bisect(array, target):
            L = 0
            R = len(array)
            while L < R:
                M = (L+R) / 2
                if array[M] < target: 
                    L = M+1
                else:
                    R = M
            return L
        heaters = sorted(heaters)
        
        result = -sys.maxint - 1
        
        for house in houses:
            index = bisect(heaters, house)
            leftDist = house - heaters[index - 1] if index > 0 else sys.maxint
            rightDist = heaters[index] - house if index < len(heaters) else sys.maxint
        
            result = max(min(leftDist, rightDist), result)
        return result
