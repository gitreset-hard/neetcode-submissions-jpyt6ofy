from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        """
            0: [],
            1: [0],
            2: [1]

        """
        # directional
        for crs, pre in prerequisites:
            courses[crs].append(pre)
        
        seen = set()

        def dfs(crs):
            if crs in seen:
                return False
            
            if courses[crs] == []: 
                return True
            
            seen.add(crs)
            for pre in courses[crs]:
                if not dfs(pre):
                    return False
            
            seen.remove(crs)
            courses[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
        

        