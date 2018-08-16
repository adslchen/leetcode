            
class Solution(object):
    def __init__(self):
        self.total = 0
    def convertBST(self, root):
        stacks = []
        head = root
        while root is not None or stacks:
            if root:
                stacks.append(root)
                root = root.right
            else:
                root = stacks.pop()
                root.val += self.total
                self.total = root.val
                root = root.left
        return head
       
