class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
                        [1,7,3,6,5,6]
            
            leftSum:  [0,1,8,11,17,22,28]
                     i:0 1 2  3  4  5 6 7 
            rightSum: [28,27,20,17,11,6,0]

        """

        
        n = len(nums)
        lSum = [0] * n
        lSum[0] = nums[0]

        rSum = [0] * n
        rSum[-1] = nums[-1]

        for i in range(1,n):
            lSum[i] = lSum[i-1] + nums[i]
        
        for i in range(n-1-1,-1,-1):
            rSum[i] = rSum[i+1] + nums[i]
        
        for i in range(n):
            if lSum[i] == rSum[i]:
                return i
        return -1
