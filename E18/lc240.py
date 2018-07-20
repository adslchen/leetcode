class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        x ,y = n-1, 0
        while y <= m-1 and x >= 0:
            if matrix[y][x] < target:
                y += 1
            elif matrix[y][x] > target:
                x -= 1
            else:
                return True
        
        
        return False
