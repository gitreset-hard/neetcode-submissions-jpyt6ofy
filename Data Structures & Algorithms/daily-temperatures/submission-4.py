class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        output = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                output[stack[-1]] = idx - stack[-1]
                stack.pop()
            
            stack.append(idx)
        
        return output