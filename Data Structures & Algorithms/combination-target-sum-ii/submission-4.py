class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        self.result = []

        def backtrack(idx, path, total):
            if total == target:
                self.result.append(list(path))
            if idx >= len(candidates) or total > target:
                return
            

            
            for j in range(idx, len(candidates)):
                if j > idx and candidates[j] == candidates[j-1]:
                    continue
                
                # optimization
                if total + candidates[j] > target:
                    break

                path.append(candidates[j])
                backtrack(j+1, path, total + candidates[j])
                path.pop()
        
        backtrack(0,[],0)
        return self.result
            