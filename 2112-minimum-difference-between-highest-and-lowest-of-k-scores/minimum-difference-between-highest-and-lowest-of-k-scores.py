class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 1: return 0
        mini = float('inf')
        nums.sort()
        l = 0
        r = k - 1
        while r < n:
            diff = nums[r] - nums[l]
            mini = min(mini, diff)
            l += 1
            r += 1
        return mini