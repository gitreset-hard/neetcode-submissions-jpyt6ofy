class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        output = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            
            while stack and temp > temperatures[stack[-1]]:
                popped = stack.pop()
                output[popped] = idx - popped

            stack.append(idx)
                    
        
        return output