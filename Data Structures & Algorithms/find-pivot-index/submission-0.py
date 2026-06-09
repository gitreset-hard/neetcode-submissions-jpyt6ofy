class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
                        [1,7,3,6,5,6]
            
            leftSum:  [0,1,8,11,17,22,28]
                     i:0 1 2  3  4  5 6 7 
            rightSum: [28,27,20,17,11,6,0]

        """

        
        n = len(nums)
        leftSum = [0] * (n+1)
        rightSum = [0] * (n+1)

        for i in range(1,n+1):
            leftSum[i] = nums[i-1] + leftSum[i-1]

        for i in range(n-1,-1,-1):
            rightSum[i] = nums[i] + rightSum[i+1]
        print(leftSum)
        print(rightSum)
        for i in range(0,n):
            if leftSum[i] == rightSum[i+1]:
                return i
        return -1
