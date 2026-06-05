class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """ 
            n: range(1,n+1)
            k: len(valid_combination)
            combination:
                order doesn't matter: [1,2] == [2,1]
            
            at each option: can chose (or not) nums[idx]

            bound is len(subArray) b/c it possible n >> k, so you can reach k in the start

            1 2 3 4
            n = 4, k = 3
            1,2,3
            1,2,  4
            1,  3,4
              2,3,4           
        """
        
        nums  = [num for num in range(1,n+1)]
        res = []
        curr = []

        def dfs(i, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return
                
            if i >= n:
                return

            # pick nums[i] and go to next idx
            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()
            dfs(i+1, curr)
        
        dfs(0,[])
        return res




