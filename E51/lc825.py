class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        a = [0]*121
        res = 0
        
        for age in ages: 
            a[age] += 1
        
        for i in range(15, 121):
            for j in range(int(i*0.5 + 8), i+1):
                
                res += a[i] * (a[j] - (i==j))
                
        return res
