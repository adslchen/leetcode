class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)
    
    def isMirror(self, left, right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        return (left.val == right.val and 
                self.isMirror(left.left, right.right) and
                self.isMirror(left.right, right.left))
