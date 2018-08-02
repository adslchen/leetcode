class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        queue = []
        queue.append(root)
        
        while queue:
            nextLevel = []
            for node in queue:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if not nextLevel : # we reach the last level
                return queue[0].val
            queue = nextLevel
            
