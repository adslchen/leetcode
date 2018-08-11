class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) -1
        maxVolume = 0
        while left < right:
            volume = (right - left) * min(height[right], height[left])
            maxVolume = max(maxVolume, volume)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
                
        return maxVolume
