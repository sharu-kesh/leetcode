class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        pre = nums[0]
        n = len(nums)
        for i in range(1, n - 1):
            if (nums[i] > pre and nums[i] > nums[i + 1]) or (nums[i] < pre and nums[i] < nums[i + 1]):
                count += 1
                pre = nums[i]
        return count
        