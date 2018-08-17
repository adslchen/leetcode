class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return
        steps = 0
        node = head
        while node.next:
            node = node.next
            steps += 1
        end = node
        node = head
 
        for i in range((steps+1)/2):
            node = node.next
        half = node
        p = half
        q = p.next
        # reverse last half list
        while q:
            t_next = q.next
            q.next = p
            p = q
            q = t_next
            
            
        print("yee")
        p = head
        q = end
        
        while p.next != q:
            t_next = p.next
            p.next = q
            p = q
            q = t_next
        q.next = None
