class Solution(object):
    def __init__(self):
        self.globalmax = float("-inf")
        
    def maxPathSum(self, root):
        self.findmax(root)
        return self.globalmax
    
    def findmax(self, node):
        if not node:
            return 0
        left = self.findmax(node.left)
        right = self.findmax(node.right)
        if left < 0: left = 0
        if right < 0: right = 0
        self.globalmax = max(left + right + node.val, self.globalmax)
        return max(left, right) + node.val
