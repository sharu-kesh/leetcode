class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        last_seen = [0] * 30
        for i in range(n - 1, -1, -1):
            for bit in range(30):
                if nums[i] & (1 << bit) > 0:
                    last_seen[bit] = i
                res[i] = max(res[i], last_seen[bit] - i + 1)
        return res