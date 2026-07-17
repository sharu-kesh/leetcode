class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_seen = 0
        for i, val in enumerate(nums):
            if val != 0:
                nums[last_seen], nums[i] = nums[i], nums[last_seen]
                last_seen += 1
        return nums
            
        