class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        mini = float('-inf')
        l = 0
        r = n - 1
        while l < r:
            sumi = nums[l] + nums[r]
            mini = max(mini, sumi)
            l += 1
            r -= 1
        return mini
        