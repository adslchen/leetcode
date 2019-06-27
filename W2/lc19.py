class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        dummy = ListNode(0)
        dummy.next = head
        first = head
        for i in range(n):
            first = first.next
        
        second = dummy
        
        while first:
            second = second.next
            first = first.next
            
        # remove the previous nth node
        second.next = second.next.next
        
        return dummy.next
            
