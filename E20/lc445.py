class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        sm = 0
        ll = ListNode(0)
        while stack1 or stack2:
            if stack1: sm += stack1.pop()
            if stack2: sm += stack2.pop()
            ll.val = sm%10
            head = ListNode(sm/10)
            head.next = ll
            ll = head
            sm /= 10
        
        return ll if ll.val != 0 else ll.next
                
