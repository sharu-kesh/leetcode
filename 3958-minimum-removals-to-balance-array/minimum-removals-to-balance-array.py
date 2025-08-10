class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        for i, val in enumerate(nums):
            ans += val > nums[ans] * k
        return ans