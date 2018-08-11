cache = {}
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        def backtrack(i, X):
            if len(X) == 1:
                return 1
            key = (i,X)
            if key in cache:
                return cache[key]
            total = 0
            for j in range(len(X)):
                if (X[j]  % i == 0 or i % X[j] == 0):
                    total += backtrack(i-1, X[:j] + X[j+1:])
            cache[key] = total
            return total
            
            
        return backtrack(N, tuple(range(1,N+1)))
