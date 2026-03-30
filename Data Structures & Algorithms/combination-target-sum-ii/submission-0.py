class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            b/c we have duplicates, we have to skipover them 
            i think each element can't be used more than once
        """
        candidates.sort()
        self.output = set()

        def dfs(idx, curPath, total):
            if total == target:
                self.output.add(tuple(curPath.copy()))
                return
            
            if idx >= len(candidates)  or total > target:
                return
                

            
            curPath.append(candidates[idx])
            dfs(idx + 1, curPath, total + candidates[idx])
            curPath.pop()
            dfs(idx + 1, curPath, total)
        
        dfs(0,[],0)
        return [list(ans) for ans in self.output ]