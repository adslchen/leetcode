class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        graph = {}
        # build the neighbor list
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            if node1 in graph:
                graph[node1].append(node2)
            else:
                graph[node1] = [node2]
            if node2 in graph:
                graph[node2].append(node1)
            else:
                graph[node2] = [node1]
                
        print(graph)
        leaves = []
        for node in graph.keys():
            if len(graph[node]) == 1:
                leaves.append(node)
        print(leaves)
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves
