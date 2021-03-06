# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        queue = []
        result = []
        queue.append(root)
        while queue and root:
            level = []
            newStack = []
            for node in queue:
                level.append(node.val)
                
                if node.left:
                    newStack.append(node.left)
                if node.right:
                    newStack.append(node.right)
            result.append(level)
            queue = newStack
        return result
