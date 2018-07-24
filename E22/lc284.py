class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
      
        self.iterator = iterator
        self.inext = None
        self.isNext = False

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.iterator.hasNext() and not self.isNext:
            return None
        if self.iterator.hasNext() and self.isNext == False:
            self.inext = self.iterator.next()
            self.isNext = True
    
        return self.inext
            

    def next(self):
        """
        :rtype: int
        """
        if self.isNext:
            self.isNext = False
        else:
            self.inext = self.iterator.next()
          
        return self.inext
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.isNext or self.iterator.hasNext():
            return True
        else:
            return False
        
