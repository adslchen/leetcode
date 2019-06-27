# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        if not head or not head.next:
            return True
        
        def reverse(node):
            prev = None
            while node:
                n = node.next
                node.next = prev
                prev = node
                node = n
                # cur = head
                # head = head.next
                # cur.next = prev
                # prev = cur
            return prev
        
        
        mid = head
        end = head
        
        while end and end.next:
            end = end.next.next
            mid = mid.next
        # if there is add node, let right half smaller
        if end:
            mid = mid.next
        
    
        rList = reverse(mid)
