class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        if n == 0:
            return []
        return self.genTree(1, n)
    
    def genTree(self, start, end):
        trees = []
        
        if start > end:
            trees.append(None)
            return trees
            
        if start == end:
            trees.append(TreeNode(start))
            return trees
        
        for i in range(start, end+1):
            leftTrees = self.genTree(start, i-1)
            rightTrees = self.genTree(i+1, end)
            print(leftTrees)
            
            for lt in leftTrees:
                for rt in rightTrees:
                    root = TreeNode(i)
                    root.left = lt
                    root.right = rt
                    trees.append(root)
                    
        return trees
