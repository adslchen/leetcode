class Solution:
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        
        if not heightMap or not heightMap[0] : return 0
        import heapq
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        ans = 0
        visit = [[ 0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    visit[i][j] = 1
                    heapq.heappush(heap, (heightMap[i][j], i, j))
    
        maxh = 0
        while heap:
            height, i, j = heapq.heappop(heap)
            maxh = max(heightMap[i][j], maxh)
            for x, y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if x < m and x >= 0 and y < n and y >= 0 and visit[x][y] == 0:
                    ans += max(0,  maxh - heightMap[x][y])
                    #ans += max(0, height - heightMap[x][y])
                    heapq.heappush(heap, (heightMap[x][y], x, y))
                    visit[x][y] = 1
        return ans
