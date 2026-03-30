class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max = [0] * n
        r_max = [0] * n
        water = [0] * n
        
        # find l_max
        l_max[0] = height[0]
        for idx in range(0,n):
            l_max[idx] = max(height[idx], l_max[idx-1])
        
        r_max[n-1] = height[n-1]
        for idx in range(n-2,-1,-1):
            r_max[idx] = max(height[idx], r_max[idx+1]) 
        
        for i in range(1,n):
            water[i] = max(min(l_max[i], r_max[i]) - height[i],0)
        print(l_max)
        print(r_max)
        print(water)
        return sum(water)