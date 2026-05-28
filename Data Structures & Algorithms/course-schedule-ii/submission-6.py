from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        courses = defaultdict(list)
        for crs, pre in prerequisites:
            courses[crs].append(pre)

        seen = set()
        visit = set()
        output = []
        """
            [0,1],[0,2],[1,2]]
            0: [1, 2]
            1: [2]
            2: []
        """
        def dfs(crs):
            if crs in seen:
                return False
            
            if crs in output:
                return True
            
            seen.add(crs)
            for pre in courses[crs]:
                if not dfs(pre):
                    return False
            
            seen.remove(crs)
            output.append(crs)
            # visit.add(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return output
            