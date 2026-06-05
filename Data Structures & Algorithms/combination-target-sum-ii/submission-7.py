class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        """
            sort candidates, then we can skip once the target exceeds
            each candidate an only be used once.
                so no : 1 1 1 1 1 1 1.
            
            # 1 2 2 4 5 6 9
        """ 

        res = []
        curr = []
        candidates.sort()
        def dfs(i, curr, curr_total):
            if curr_total == target:
                res.append(curr.copy())
                return
            
            for j in range(i, len(candidates)):
                # find duplciates
                # j > i after stack starts retracing, otherwise j == i down the tree
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                
                if curr_total + candidates[j] > target:
                    break
                
                curr.append(candidates[j])
                dfs(j + 1, curr, curr_total + candidates[j])
                curr.pop()

            
        dfs(0,curr, 0)
        return res