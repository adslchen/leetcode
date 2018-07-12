class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.rStack = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.rStack:
            self.rStack.append(self.stack.pop())
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        
     
        item = self.rStack.pop()
        
        if len(self.rStack) == 0:
        
            for i in range(len(self.stack)):
                self.rStack.append(self.stack.pop())
                
        return item
                
        
        
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.rStack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return (len(self.rStack)  == 0)
