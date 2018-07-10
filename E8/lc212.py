class TriesNode(object):
    def __init__(self):
        self.next = [None]*26
        self.word = None

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        if len(board) == 0:
            return []
        m, n = len(board), len(board[0])
        head = self.buildTries(words)
        result = []
        for i in range(m):
            for j in range(n):
                self.DFS(board, i, j, head,result)
                
        return result
                
    def DFS(self, board, i, j, p, result):
        c = board[i][j]
        
        ascii = ord(c) - ord('a')
        if c == '#' or p.next[ascii] == None:
            return 
        p = p.next[ascii]
        if p.word :
            result.append(p.word)
            p.word = None
        m, n = len(board), len(board[0])
            
        board[i][j] = '#'
        if i > 0 : self.DFS(board, i-1, j, p, result)
        if i < m-1: self.DFS(board, i+1, j, p, result)
        if j > 0 : self.DFS(board, i, j-1, p, result)
        if j < n-1: self.DFS(board, i, j+1, p, result)
        board[i][j] = c
        
        
    def buildTries(self, words):
        head = TriesNode()
        for word in words:
            p = head
            for i in range(len(word)):
                ascii = ord(word[i]) - ord('a')
                if p.next[ascii] == None:
                    p.next[ascii] = TriesNode()
                p = p.next[ascii]
            p.word = word
        return head
        
