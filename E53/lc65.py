class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        n = len(s)
        
        while i < n and s[i] == ' ': 
            i += 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            i += 1
        isNum = False
            
        while i < n and s[i].isdigit():
            i += 1
            isNum = True
        
        if (i < n and s[i] == '.'):
            i += 1
            while i < n and s[i].isdigit():
                i += 1
                isNum = True
        
        if isNum and i < n and s[i] == 'e':
            i += 1
            isNum = False
            if i < n and (s[i] == '+' or s[i] == '-'):
                i += 1
            while i < n and s[i].isdigit():
                i += 1
                isNum = True
        
        while i < n and s[i] == ' ':
            i += 1
        return isNum and i==n
                
            
