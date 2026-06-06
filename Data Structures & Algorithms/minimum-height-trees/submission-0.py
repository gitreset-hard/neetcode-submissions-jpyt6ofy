from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
            undirected graph, [0,n] == 0 -> n-1
            no cycles
            edges: [a,b]:  a <-> b
            x: chose any node can be root

            task:
                find minimum height (depth of recursion) of tree
                can have more than 1 ans with equivalent MHT
            
            appraoch:
                1. build graph
                2. dfs from each node to find depth
                    - optimizations:
                        1. FALSE: maybe the MHT is guranteed to be the node with the most edges, 
                                        so can reduce the num of traversals needed
            ex:
            n = 5
            0: [1]
            1: [0,3,4]
            2: [3]
            3: [2,1]
            4: [1]           
        
        """
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        

        def dfs(curr, parent):
            max_depth = 0
            for edge in graph[curr]:
                if edge != parent:
                    max_depth = max(max_depth, dfs(edge, curr) + 1)
            return max_depth



        nodeDepth = {x:[] for x in range(n)}
        for idx in range(n):
            nodeDepth[dfs(idx,-1)].append(idx)
        
        res = []
        for depth, nodes in nodeDepth.items():  
            if len(nodes) > 0:
                return nodes
