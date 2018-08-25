class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stacks = []
        paren = {"}":"{", "]": "[", ")":"("}
        for i in range(len(s)):
            if s[i] in "{[(":
                stacks.append(s[i])
            elif s[i] in "}])":
                if not stacks:
                    return False
                last = stacks.pop()
                if last != paren[s[i]]:
                    return False
    
        return not stacks
        
