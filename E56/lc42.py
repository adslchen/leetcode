class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        if not height: return 0
        leftmax = [0] * len(height)
        rightmax = [0] * len(height)
        
        result = 0
        
        # construct leftmax
        leftmax[0] = height[0]
        for i in range(1, len(height)):
            leftmax[i] = max(height[i], leftmax[i-1])
            
            
        rightmax[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            rightmax[i] = max(rightmax[i+1], height[i])
            
        # find intersect
        for i in range(len(height)):
            result += min(leftmax[i], rightmax[i]) - height[i]
            
        return result
        
        stack = []
        ans = 0
        
        for current in range(len(height)):
            while stack and height[current] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                dist = current - stack[-1] -1
                bound = min(height[current], height[stack[-1]]) - height[top]
                ans += dist * bound
            stack.append(current)
        return ans"""
        
        left= 0
        right = len(height) -1
        ans = 0
        leftmax, rightmax = 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] <= leftmax:
                    ans += leftmax - height[left]
                else:
                    leftmax = height[left]
                left += 1
            else:
                if height[right] <= rightmax:
                    ans += rightmax - height[right]
                else:
                    rightmax = height[right]
                right -= 1
        return ans
