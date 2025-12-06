class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False
        half = total // 2

        def dp(i, curr, memo: dict):
            if i == n or curr > half:
                return False
            if curr == half:
                return True
            if (i, curr) not in memo:
                take = dp(i+1, curr + nums[i], memo)
                skip = dp(i+1, curr, memo)
                memo[(i, curr)] = take or skip
            return memo[(i, curr)]
        return dp(0, 0, {})