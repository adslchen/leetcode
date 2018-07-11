class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
       
        n = len(height)
        leftMax, rightMax = [0 for i in range(n)], [ 0 for i in range(n)]
        leftmax = 0
        for i in range(n):
            leftmax = max(height[i], leftmax)
            leftMax[i] = leftmax
            
        rightmax = 0
        for i in range(n-1,-1,-1):
            rightmax = max(height[i], rightmax)
            rightMax[i] = rightmax
            
        ans = 0
        for i in range(n):
            ans += min(rightMax[i], leftMax[i]) - height[i]
            
        
            
        return ans
