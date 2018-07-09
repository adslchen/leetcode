class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        bucket = [0] * 26
        for i in range(len(tasks)):
            bucket[ord(tasks[i]) - ord('A')] += 1
        
        bucket = sorted(bucket)
        
        time = 0
        while bucket[25] > 0:
            index = 0
            while index <= n:
                if bucket[25] == 0:
                    break
                if index < 26 and bucket[25-index] > 0:
                    bucket[25-index] -= 1
                time += 1
                index += 1
            bucket = sorted(bucket)
        return time
