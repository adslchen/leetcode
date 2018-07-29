class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        mapping = {'L':(-1,0),'R':(1,0),'U':(0,-1),'D':(0,1)}
        
        dist = [0,0]
        
        for i in range(len(moves)):
            dist[0] += mapping[moves[i]][0]
            dist[1] += mapping[moves[i]][1]
        
        if dist[0] == 0 and dist[1] == 0:
            return True
        else:
            return False
