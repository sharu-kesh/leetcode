from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        maxLen = 0
        l = 0
        r = 0
        n = len(nums)
        while r < n:
            freq[nums[r]] += 1
            while freq[nums[r]] > k:
                freq[nums[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen
        