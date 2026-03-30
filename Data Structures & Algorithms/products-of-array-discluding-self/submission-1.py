
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        brute force: product without each element. O(n^2)

        optimized: total product / cur element but can have div by 0 error

        arr  1  2  4  6
        pre  1  1  2  8
        suf  48 24 6  1
        ans  48 24 12 8
        """
        n = len(nums)
        ans = [1] * n
        pre = [1] * n
        suf = [1] * n

        for i in range(1,n):
            pre[i] = pre[i-1] * nums[i-1]
        
        for i in range(n-2,-1,-1):
            suf[i] = suf[i+1] * nums[i+1]
        
        for i in range(n):
            ans[i] = pre[i] * suf[i]
        
        return ans

