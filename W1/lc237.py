# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node, n):
        """
        :type node: ListNode
        :type n: int
        :rtype: None Do not return anything, modify node in-place instead.
        """
        
        
        dummy = ListNode(0)
        dummy.next= node
        p = dummy
        cur = node
        while cur:
            if cur.val == n:
                self.delete(cur)
                break
            p = cur
            cur = cur.next
        node = dummy.next
        
        
        
    def delete(self, node):
        node.val = node.next.val
        node.next = node.next.next
