class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        total = len1 + len2
        target = total // 2
       

        l , r = 0,0
        currVal, prevVal = 0,0
        while l + r <= target:
            prevVal = currVal
            if r >= len2 or (l < len1 and nums1[l] <= nums2[r]):
                currVal = nums1[l]
                l += 1
            else:
                currVal = nums2[r]
                r+= 1

        if total % 2 == 1:
            return float(currVal)
        else:
            return (currVal + prevVal) / 2.0
        

