class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        graph = [ [] for _ in range(numCourses) ]
        visit = [ 0 for _ in range(numCourses) ]
        
        reStack = []
        
        for x, y in prerequisites:
            graph[x].append(y)
        
        def DFS(node, visit, reStack):
            if visit[node] == -1:
                return False
            
            if visit[node] == 1:
                return True
            
            visit[node] = -1
            for neighbor in graph[node]:
                if not DFS(neighbor, visit, reStack):
                    return False
            visit[node] = 1
            reStack.append(node)
            return True

        for i in range(numCourses):
        
            if not DFS(i, visit, reStack):
                return []
            elif len(reStack) == numCourses:
                break
                
            
        return reStack
