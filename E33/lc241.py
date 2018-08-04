class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        result = []
        
        for i in range(len(input)):
            if input[i] == '+' or input[i] == '-' or input[i] == '*':
                part1 = self.diffWaysToCompute(input[:i])
                part2 = self.diffWaysToCompute(input[i+1:])
                
                for p1 in part1:
                    for p2 in part2:
                        if input[i] == '+':
                            result.append(p1+p2)
                        elif input[i] == '-':
                            result.append(p1-p2)
                        elif input[i] == '*':
                            result.append(p1*p2)
                            
        if not result :
            return [int(input)]
                            
        return result
