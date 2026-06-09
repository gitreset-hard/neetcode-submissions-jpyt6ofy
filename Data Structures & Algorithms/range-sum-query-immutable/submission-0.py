class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        curr = 0
        for num in nums:
            curr+= num
            self.prefix.append(curr)

    def sumRange(self, left: int, right: int) -> int:
        rSum = self.prefix[right]
        
        # arr: [-2,0,3,-5,2,-1]
              # 0 -2,0,1,-4,-2,-3
             # 0-> 2 = 1 - (0)
             # 2->5 = sum(3,-5,2,-1) = -1 -> -3 - -2
        
        lSum = self.prefix[left-1] if left > 0 else 0 # b/c we want to include the left index, so subtract one to get it up to that point
        return rSum - lSum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)