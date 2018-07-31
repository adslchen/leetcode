class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
        if int(s) == 0: return 0
        dp = [0] * (n+1)

        dp[0] = 1
        if s[0] != "0":
            # to avoid "01","02.." that start with 0
            dp[1] = 1
        
        for i in range(2, n+1):
            sm = 0
            if s[i-1] != "0":
                sm = dp[i-1]
            if int(s[i-2:i]) <= 26 and int(s[i-2:i]) > 0 and s[i-2] != "0":
                # we should avoid:
                # 1. > 26
                # 2. <= 0
                # 3. "02", "04"
                sm += dp[i-2]
            dp[i] = sm
            
        return dp[n]
            
