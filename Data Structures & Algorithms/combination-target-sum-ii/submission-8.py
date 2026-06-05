class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            1,2,2,2,2,4,5,6,9 , 
            target = 8
            1,2,5 , just once
            2,2,2,2
            2,2,4
            2,6

            can only use a number once
            sort it so we can end traversal early per iter
        """
        candidates.sort()
        res = []
        curr = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            """ 
                         1,2,2,2,4,5,6,7
            i=0, j= 0    1
            i=1, j= 1      2
            ...              2 2
            i=4, j=4             4      > 8 : return -> don't look at 4+ b/c all > target
            ... 
            i=4  j =1                             
                      
            """
            for j in range(i, len(candidates)):
                # skip after the first full depth recursion if there is a repeat number, 
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                
                if total + candidates[j] > target:
                    break
                
                curr.append(candidates[j])
                dfs(j+1,curr, total + candidates[j])
                curr.pop()

        
        dfs(0, curr, 0)
        return res
            





