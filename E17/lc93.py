class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        
        def dfs(path):
            if path[-1] > len(s):
                return
            num = int(s[path[-2]:path[-1]]) 
            length = path[-1] - path[-2]
            if num < 0 or num > 255 or (length > 1 and s[path[-2]] == '0'):
                return
            if len(path) == 5:
                if path[-1] == len(s):
                    result.append(path)
                return
            
            dfs(path + [path[-1] + 1])
            dfs(path + [path[-1] + 2])
            dfs(path + [path[-1] + 3])
            
        dfs([0]+ [1])
        dfs([0]+[2])
        dfs([0]+ [3])
        
        ans = []
        for path in result:
            ip = s[path[0]:path[1]] + "." + s[path[1]:path[2]] + "." + s[path[2]:path[3]] + "." + s[path[3]:path[4]]
            ans.append(ip)
        return ans
        
