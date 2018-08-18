class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.DFS(image, sr, sc, newColor)
        return image
        
    def DFS(self, image, r, c, newColor):
        origin_color = image[r][c]
        m, n = len(image), len(image[0])
       
        
        neighbor = [(1,0),(-1,0),(0,1),(0,-1)]
        image[r][c] = -1
        for nei in neighbor:
            R = r + nei[0]
            C = c + nei[1]
            if R < m and R >=0 and C < n and C >=0 and image[R][C] == origin_color :
                
                self.DFS(image, R, C, newColor)
        image[r][c] = newColor
        return
        
