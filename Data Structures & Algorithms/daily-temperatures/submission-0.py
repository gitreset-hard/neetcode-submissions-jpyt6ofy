class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
            brute: for each temp, iterate to find the next warm day
            better: use monotinc decreasing stack from l -> 4

            [30,30,29,38,36,35,40,28]

        """
        stack = []
        ans = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                ans[stack[-1]] = idx - stack[-1]
                stack.pop()
            
            stack.append(idx)
        
        return ans
