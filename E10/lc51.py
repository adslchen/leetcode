class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.table = [['.' for j in range(n)] for i in range(n)]
        self.solution = []
        self.solve_start_at(0)
        return self.solution
    
    def solve_start_at(self,row_index):
        flag = False
        for i in range(self.n):
            if self.check_position(row_index,i):
                self.table[row_index][i] = 'Q'
                if row_index == self.n-1:
                    self.solution.append([''.join(row) for row in self.table])
                    flag = True
                elif self.solve_start_at(row_index+1):
                    flag = True
                self.table[row_index][i] = '.'
            else:continue
        return flag
    
    def check_position(self,i,j):
        for k in range(i):
            if self.table[k][j] == 'Q':return False
        p,k = i-1,j-1
        while p>=0 and k>=0:
            if self.table[p][k] == 'Q':return False
            p,k = p-1,k-1
        p,k = i-1,j+1
        while p>= 0 and k<=self.n-1:
            if self.table[p][k] == 'Q':return False
            p,k = p-1,k+1
        return True
