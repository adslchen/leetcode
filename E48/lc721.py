class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        graph = {}
        for person, account in enumerate(accounts):
            graph[person] = []
            for i in range(1,len(account)):
                if account[i] not in graph:
                    graph[account[i]] = []
                graph[account[i]].append(person)
                graph[person].append(account[i])
            
                
        visit = {}
        #print(graph)
        ans = []
        for person, account in enumerate(accounts):
            queue = []
            queue.append(person)
            acc = []
            while queue:
                
                q = queue.pop()
                for node in graph[q]:
                    if node not in visit:
                        queue.append(node)
                if type(q) == unicode and q not in acc:
                    acc.append(q)
                visit[q] = True
                
            if acc:
                ans.append([account[0]]+sorted(acc))
            
        return ans
