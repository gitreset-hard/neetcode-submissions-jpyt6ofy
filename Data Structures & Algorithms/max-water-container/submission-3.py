class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        l, r = 0, len(heights) - 1

        while l < r:

            w = r - l
            h = min(heights[r],heights[l])
            ans = max(ans, w*h)
            if heights[l] <= heights[r]:
                l +=1
            else:
                r -=1
            
        return ans