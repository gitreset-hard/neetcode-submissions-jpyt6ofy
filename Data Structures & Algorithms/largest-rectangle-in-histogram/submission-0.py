class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """

        """

        n = len(heights)
        left_next_smallest = [-1]* n # left bound is base case
        
        right_next_smallest = [n]* n # if no smaller value found, then right bound is the base case
        ans = [0]*n
        # right_next_smallest[n-1] = 0
        # right next smallest: left -> pass 
        # mono increasing stack
        stack = []
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                right_next_smallest[stack[-1]] = i
                stack.pop()
            stack.append(i)

        # left next smallest: right -> leff pass
        stack = []
        for i in range(n-1,-1,-1):

            while stack and heights[i] < heights[stack[-1]]:
                left_next_smallest[stack[-1]] = i 
                stack.pop()
            
            stack.append(i)

        print(right_next_smallest)
        print(left_next_smallest)
        # ans = [7, 6, 7, 8, 8, 4]
        for i in range(n):
            # area = w * h
            # w = right - left
            w = right_next_smallest[i] - left_next_smallest[i] - 1
            ans[i] = w * heights[i]
        
        return max(ans)



        
        


