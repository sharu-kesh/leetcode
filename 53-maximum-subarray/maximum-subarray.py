class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        tot = 0
        for i in nums:
            if tot < 0:
                tot = 0
            tot += i
            res = max(res, tot)
        return res