class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        """
        if head == None: return None
        randomMap = {}
        dummyHead = RandomListNode(0)
        copyNode = dummyHead
        node = head
        while node:
            copyNode.next = RandomListNode(node.label)
            randomMap[node] = copyNode.next
            node = node.next
            copyNode = copyNode.next
            
        p = dummyHead
        node = head
        print(node.random)
        while node:
            if node.random == None:
                p.next.random = None
            else:
                p.next.random = randomMap[node.random]
            p = p.next
            node = node.next
        return dummyHead.next"""
        
        node = head
        while node:
            copyNode = RandomListNode(node.label)
            temp_next = node.next
            copyNode.next = node.next
            node.next = copyNode
            node = temp_next
        
        node = head
        while node:
            if node.random != None:
                node.next.random = node.random.next
            node = node.next.next
        
        node = head
        dummyHead = node.next if node != None else None
        
        
        while node:
            copy = node.next
            node.next = copy.next
            node = node.next
            copy.next = node.next if node != None else None
            
        return dummyHead
