class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        mapping = ["abc", "def", "ghi","jkl","mno","pqrs","tuv","wxyz"]
        result = []
        n_digits = len(digits)
        def backtrack(paths = '', index=0):
            if len(paths) == n_digits:
                result.append(paths)
                return
            
            candidate = mapping[int(digits[index]) - 2]
            for i in range(len(candidate)):
                paths += candidate[i]
                backtrack(paths, index + 1)
                paths = paths[:-1] 
            
        backtrack()
            
        return result
