class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        sm = 0
        left2right = [1] * len(ratings)
        right2left = [1] * len(ratings)
        
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                left2right[i] = left2right[i-1] + 1
        
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right2left[i] = right2left[i+1] + 1
                
        
        for i in range(len(left2right)):
            sm += max(left2right[i], right2left[i])
            
        return sm
