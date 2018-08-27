from collections import deque
import math
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squared = [ val**2 for val in range(1, int(math.sqrt(n))+1)]
        
        queue = deque()
        queue.append([0,0])
        visit = [0] * (n+1)
        visit[0] = 1
        while queue:
            val, s = queue.popleft()
            for i in squared:
                if val + i == n:
                    return s+1
                elif val + i > n:
                    continue
                else:
                    if visit[val+i] == 0:
                        queue.append([val+i, s+1])
                        visit[val+i] = 1
                
