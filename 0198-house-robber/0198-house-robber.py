class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev2 = 0
        prev = nums[0]
        for i in range(1, n):
            take = nums[i] + prev2
            nottake = prev
            cur = max(take, nottake)
            prev2 = prev
            prev = cur
        return prev