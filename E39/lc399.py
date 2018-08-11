class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        adjacent = {}
        # construct graph
        
        for idx, eq in enumerate(equations):
            if eq[0] not in adjacent:
                adjacent[eq[0]] = []
            if eq[1] not in adjacent:
                adjacent[eq[1]] = []
            adjacent[eq[0]].append((eq[1], float(values[idx])))
            adjacent[eq[1]].append((eq[0], float(1/values[idx])))
        
        ans = []
        for q in queries:
            start = q[0]
            end = q[1]
            if start not in adjacent or end not in adjacent:
                ans.append(-1.0)
                continue
            queue = []
            queue.append((start,1.0))
            visited = {}
            result = -1.0
            while queue and result == -1.0:
                nextnode = []
                for qq, value in queue:
                    if qq in visited:
                        continue
                    if qq == end:
                        result = value
                        break
                    neibors = adjacent[qq]
                    for nei, cost in neibors:
                        nextnode.append((nei, value * cost))
                    visited[qq] = True
                    
                queue = nextnode
            ans.append(result)
        return ans
                    
