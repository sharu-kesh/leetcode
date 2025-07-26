class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def findMax(nums):
            n = len(nums)
            prev = nums[0]
            prev2 = 0
            for i in range(1, n):
                take = nums[i]
                if i > 1: take += prev2
                cur = max(take, prev)
                prev2 = prev
                prev = cur
            return prev

        return max(findMax(nums[:-1]), findMax(nums[1:]))
        