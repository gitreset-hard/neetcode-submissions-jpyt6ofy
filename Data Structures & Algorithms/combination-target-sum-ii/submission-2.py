class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []


        def dfs(idx, curPath, total):
            if total == target:
                res.append(curPath.copy())
                return

            if total > target or idx >= len(candidates):
                return
            
            for j in range(idx,len(candidates)):
                if j > idx and candidates[j] == candidates[j-1]:
                    continue
                
                curPath.append(candidates[j])
                dfs(j+ 1, curPath, total + candidates[j])
                curPath.pop()
        
        dfs(0,[],0)
        return res
                