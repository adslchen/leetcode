class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        m, n = len(matrix), len(matrix[0])
        row, col = 0, -1
        result = []
        
        while n > 0:
            for i in range(n):
                col += 1
                result.append(matrix[row][col])
            m -= 1
            if m <= 0 :
                break
            for i in range(m):
                row += 1
                result.append(matrix[row][col])
            n -= 1
            if n <= 0:
                break
            for i in range(n):
                col -= 1
                result.append(matrix[row][col])
            m -= 1
            if m <= 0:
                break
            for i in range(m):
                row -= 1
                result.append(matrix[row][col])
            n -= 1
