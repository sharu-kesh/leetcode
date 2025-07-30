class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        maxi = max(nums)
        count = 0
        for i in nums:
            if i == maxi:
                count += 1
            else:
                count = 0
            res = max(res, count)
        return res
        