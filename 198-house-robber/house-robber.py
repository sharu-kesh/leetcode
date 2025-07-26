class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def f(index):
            if index < 0: return 0
            if dp[index] != -1 : return dp[index]
            take = nums[index] + f(index - 2)
            nottake = f(index - 1)
            dp[index] = max(take, nottake)
            return dp[index]
        dp = [-1] * n
        return f(n - 1)
        