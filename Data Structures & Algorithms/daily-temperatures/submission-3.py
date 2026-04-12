class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] *  len(temperatures)

        for idx, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                greater = stack.pop()
                result[greater] = idx - greater
            
            stack.append(idx)
        
        return result

