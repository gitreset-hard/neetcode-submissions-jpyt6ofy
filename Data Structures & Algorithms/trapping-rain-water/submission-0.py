class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max = [0] * n
        r_max = [0] * n
        water = [0] * n
        l_max[0] = r_max[n-1] = 1
        # find l_max
        max_so_far = height[0]
        for i in range(1,n):
            max_so_far = max(max_so_far, height[i])
            l_max[i] = max_so_far

        # find r_max
        max_so_far = height[n-1]
        for i in range(n-2,-1,-1):
            max_so_far = max(max_so_far,height[i])
            r_max[i] = max_so_far

        # calc water at each step
        for i in range(1,n-1):
            cur = min(l_max[i], r_max[i]) - height[i]
            water[i] = cur
        
        return sum(water)