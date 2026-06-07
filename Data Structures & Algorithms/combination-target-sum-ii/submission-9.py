class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            1 2 2 4 5 6 9
            s
                  e 
        """
        
        candidates.sort()
        res = []
        curr = []

        def backtrack(start, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            for end in range(start, len(candidates)):
                
                if end > start and candidates[end] == candidates[end-1]:
                    continue # skip duplicates
                if total + candidates[end] > target:
                    break # the recursion

                curr.append(candidates[end])
                backtrack(end + 1, curr, total+candidates[end])
                curr.pop()
        
        backtrack(0,curr,0)
        return res
        
