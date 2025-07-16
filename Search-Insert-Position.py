class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        result = 0
        for i in range(len(nums) - 1, -1, -1):
            if target > nums[i]:
                result = i + 1
                break
            if target == nums[i]:
                result = i
                break
        return result