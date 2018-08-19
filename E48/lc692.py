from collections import Counter
import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = Counter(words)
        heap = [(-freq, word) for word, freq in counter.iteritems()]
        heapq.heapify(heap)
        
        return [heapq.heappop(heap)[1] for i in range(k)]
