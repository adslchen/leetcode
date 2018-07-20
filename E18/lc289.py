class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        neighbor = []
        for i in [-1,0,1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                neighbor.append((i,j))
                
        m, n = len(board), len(board[0])
        temp_board = [[d for d in c] for c in board]
        
        count = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                for nei in neighbor:
                    I,J = i + nei[0], j+nei[1]
                    if I < 0 or I >= m or J < 0 or J >= n:
                        continue
                    if board[I][J] == 1:
                        count[i][j] += 1
                        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    if count[i][j] < 2:
                        board[i][j] = 0
                    elif count[i][j] >= 2 and count[i][j] <= 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                    continue
                if board[i][j] == 0:
                    if count[i][j] == 3:
                        board[i][j] = 1
