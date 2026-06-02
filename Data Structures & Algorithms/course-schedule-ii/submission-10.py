from collections import defaultdict 
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
            - if cycle -> invalid
            - directed graph
            - dfs will have us find the empty course that must be taken first?
            - must do multisource dfs 
            0: []
            1: [0]
            2: []
        """

        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        curr_path = set() # cycle detection
        visited = set() # global
        res = []

        def dfs(crs):
            # base case
            if crs in visited:
                return True

            if crs in curr_path:
                return False
            curr_path.add(crs)

            for neighbor in adj[crs]:
                if not dfs(neighbor):
                    return False
            
            curr_path.remove(crs)
            res.append(crs)
            visited.add(crs)
            return True
            
        
        for num in range(numCourses):
            if not dfs(num):
                return []
        
        return res
        
        

        