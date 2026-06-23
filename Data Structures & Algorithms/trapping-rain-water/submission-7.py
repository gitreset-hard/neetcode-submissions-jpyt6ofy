class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max = [0] * n
        r_max = [0] * n
        l_max[0] = height[0]
        r_max[n-1] = height[n-1]
        
        for left in range(1,n-1):
            right = -left -1 # right pointer

            l_max[left] = max(height[left], l_max[left-1])
            r_max[right] = max(height[right], r_max[right +1])
        
        ans = 0
        for i in range(n):
            pot = max(min(l_max[i], r_max[i]) - height[i], 0)
            ans += pot
        
        return ans


