class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def dp(i, j, memo: dict):
            if i == j:
                return 0
            if i == j-1:
                return nums[j-1]
            if (i, j) not in memo:
                rob = nums[i] + dp(i+2, j, memo)
                skip = dp(i+1, j, memo)
                memo[(i, j)] = max(rob, skip)
            return memo[(i, j)]
        return max(dp(0, n-1, {}), dp(1, n, {}))