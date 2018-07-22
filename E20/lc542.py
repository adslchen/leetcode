class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        
        count = [ [0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                visit = {}
                if matrix[i][j] == 1:
                    dist = self.BFS(matrix,i,j)
                    count[i][j] = dist
                    
        return count
                    
            
        
        
        
        
    def BFS(self, matrix,i,j):
        
        m, n = len(matrix), len(matrix[0])
        queue = []
        visit = {}
        neighbors = [(-1,0),(1,0),(0,1),(0,-1)]
        queue.append((i,j))
        level = 0
        while queue:
            newQueue = []
            
            for x, y in queue:
          
                visit[x,y] = True
                if matrix[x][y] == 0:
                    return level
                for n1, n2 in neighbors:
                    
                    I = n1+x
                    J = n2+y
                    if I < 0 or J < 0 or I >= m or J >= n:
                        continue
                    if (I,J) in visit:
                        continue
                        
                    newQueue.append((I,J))
                    
                    
            level += 1
            queue = newQueue
                    
