class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        res = 0
        for j in range(k):
            dp = [0] * k
            for i in range(len(nums)):
                mod = nums[i] % k
                pos = (j - mod + k) % k
                dp[mod] = dp[pos] + 1
            res = max(res, max(dp))
        return res

        