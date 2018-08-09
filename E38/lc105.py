
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        if len(preorder) == 0:return None
        root_node = TreeNode(preorder[0])
        j = inorder.index(preorder[0])
        root_node.left  = self.buildTree(preorder[1:j+1],inorder[0:j])
        root_node.right = self.buildTree(preorder[j+1:],inorder[j+1:])
        return root_node
        
            
