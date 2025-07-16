class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        length = len(nums)
        mid = length // 2
        if length % 2 == 1:
            return float(nums[mid])
        else:
            return float(nums[mid-1]+nums[mid]) / 2.0
        