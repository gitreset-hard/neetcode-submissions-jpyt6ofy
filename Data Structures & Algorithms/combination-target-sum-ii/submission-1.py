class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            b/c we have duplicates, we have to skipover them 
            i think each element can't be used more than once
        """
        candidates.sort()
        output = []

        def dfs(idx, curPath, total):
            
            if total == target:
                output.append(curPath.copy())
                return 
            
            if idx > len(candidates) or total > target:
                return None
            
            for i in range(idx, len(candidates)):
                if i >idx and candidates[i] == candidates[i-1]:
                    continue
                

                curPath.append(candidates[i])
                dfs(i+1, curPath, total + candidates[i])
                curPath.pop()

        dfs(0,[],0)
        return output