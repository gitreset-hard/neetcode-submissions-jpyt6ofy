class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
            2 4 -3 5
            contiguous
            ans= 2*4

            can we keep a min and max?
            a min can turn to max with a negative sign

            2 4 -3 -5 
              8
                -24
                    120
        """
        currMin = currMax = nums[0]
        ans = nums[0]
        for i , val in enumerate(nums):
            if i == 0: continue

            prevMax = currMax
            
            currMax = max(val, val*prevMax, val*currMin)
            currMin = min(val, val*prevMax, val*currMin)

            ans = max(ans, currMax) #, currMin)

        return ans












