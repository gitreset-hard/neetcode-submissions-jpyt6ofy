class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        # iterative
        out = [[]]
        for num in nums:

            out += [sub + [num] for sub in out]
        
        return out
        """

        # backtracking
        out = []
        def dfs(idx,curPath):
            if idx >= len(nums):
                print("F", curPath, idx)
                out.append(curPath.copy())
                return
            curPath.append(nums[idx])
            print(1, curPath, idx+1)
            dfs(idx +1 , curPath)
            curPath.pop()
            print(2, curPath, idx+ 1)
            dfs(idx + 1, curPath)

        dfs(0,[])
        return out