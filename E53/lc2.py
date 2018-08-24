class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = 0
        result = ListNode(0)
        dummyhead = result
        while(l1 != None or l2 != None):
            sum /= 10
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            result.next = ListNode(sum%10)
            result = result.next
        
        if sum/10 >= 1:
            result.next = ListNode(sum/10)
            
        return dummyhead.next
              
