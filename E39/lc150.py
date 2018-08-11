class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        
        for item in tokens:
            
            if item in "+-/*":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(self.operator(item, a,b)))
            else:
                stack.append(int(item))
        print(stack) 
        return stack.pop()
                
    def operator(self, item, a,b):
        if item == '+':
            return a+b
        elif item == '-':
            return a-b
        elif item == '*':
            return a*b
        elif item == '/':
            return a/b
