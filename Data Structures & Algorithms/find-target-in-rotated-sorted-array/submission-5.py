class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        pivot = l

        def binary_search(l,r):
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        
        ans = binary_search(0, pivot-1)
        if ans != -1: return ans

        return binary_search(pivot, len(nums) -1)
                
        