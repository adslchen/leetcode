class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0: return []
        m, n = len(matrix), len(matrix[0])
        
      
        ans = []
        c = 0
        r = 0
        
        for i in range(m*n):
            ans.append(matrix[r][c])
            if (c + r) % 2 == 0: # move up
                if c == n-1: r += 1
                elif r == 0: c += 1
                else: 
                    r -= 1
                    c += 1
            else: # move down
                if r == m-1: c += 1
                elif c == 0: r += 1
                else:
                    r += 1
                    c -= 1
        return ans
