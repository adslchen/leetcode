class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        
        """
        if len(board) == 0 : return False
        if not word: return True
        m, n = len(board), len(board[0])
        visit = {} 
        for y in range(m):
            for x in range(n):
                if self.DFS(board, y, x, word, visit):
                    return True
        return False
                    
                    
    def DFS(self, board, y, x, word, visit):
        if word == '':
            return True
        key = 'y' + str(y) + 'x' + str(x)
        if visit.get(key):
            return 
        
        
        m, n = len(board), len(board[0])
        if y > m-1 or y < 0 or x > n-1 or x < 0:
            return
        if board[y][x] != word[0]:
            return 
        
        neighbors = [(-1,0),(0,-1),(1,0),(0,1)]
        visit[key] = True
        for neibor in neighbors:
            newY = y+neibor[0]
            newX = x+neibor[1]
            if self.DFS(board, newY, newX, word[1:], visit):
                return True
            #key2 = 'y'+ str(newY) + 'x' + str(newX)
        visit[key] = False
