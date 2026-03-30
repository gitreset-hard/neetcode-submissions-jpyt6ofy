class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        trapped = [0] * n

        cur_max = height[0]
        for idx in range(1,n):
            cur_max = max(cur_max, height[idx])
            left_max[idx] = cur_max
        
        cur_max = height[n-1]
        for idx in range(n-1-1,-1,-1):
            cur_max = max(cur_max, height[idx])
            right_max[idx] = max(cur_max, height[idx])
        
        print(left_max)
        print(right_max)
        # find left and right max per idx
        for idx in range(1,n-1):
            water = min(left_max[idx], right_max[idx]) - height[idx]
            trapped[idx] = water if water > 0 else 0
        
        return sum(trapped)
