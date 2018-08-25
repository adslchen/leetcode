class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def backtrack(paths='', left = 0, right = 0):
            if len(paths) == n*2:
                result.append(paths)
            else:
                if left < n:
                    backtrack(paths + '(', left+1, right)
                if right < left:
                    backtrack(paths + ')', left, right+1 )
            
            
            
            
            
        backtrack()
        return result
