class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            i = abs(i)
            if nums[i - 1] > 0:
                nums[i - 1] = -1 * nums[i - 1]
        for i, val in enumerate(nums):
            if val > 0:
                res.append(i + 1)
        return res
        