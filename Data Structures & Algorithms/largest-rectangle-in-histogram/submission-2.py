class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        ans = 0

        right_pass = [len(heights)] * len(heights)
        stack = []
        for idx, height in enumerate(heights):
            while stack and  height < heights[stack[-1]]:
                right_pass[stack[-1]] = idx
                stack.pop()
            stack.append(idx)
        
        left_pass = [-1] * len(heights)
        stack = []
        for idx in range(len(heights)-1,-1,-1):
            while stack and heights[idx] < heights[stack[-1]]:
                left_pass[stack[-1]] = idx
                stack.pop()
            stack.append(idx)
        
        ans = 0
        for i in range(len(heights)):
            width = right_pass[i] - left_pass[i] - 1
            area = width * heights[i]
            ans = max(ans, area)
        
        return ans

