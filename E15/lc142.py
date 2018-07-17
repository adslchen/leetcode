class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
            
        if fast == None or fast.next == None:
            return None
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
