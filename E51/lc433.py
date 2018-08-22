class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        # building graph
        graph = {}
        for idx, gene1 in enumerate(bank):
            for i in range(8):
                key = gene1[:i] + "_" + gene1[i+1:]
                if key not in graph:
                    graph[key] = []
                graph[key].append(gene1)
        
        # bfs
        queue = []
        queue.append(start)
        visit = {}
        mutations = 0
        while queue:
            nextLevel = []
            
            for gene in queue:
                if gene in visit:
                    continue
                if gene == end:
                    return mutations
                for i in range(8):
                    key = gene[:i]+"_"+gene[i+1:]
                    if key in graph:
                        nextLevel += graph[key]
                visit[gene] = True
            queue = nextLevel
            mutations += 1
        return -1
