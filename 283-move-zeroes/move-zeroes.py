class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastidx = -1
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[lastidx + 1] = nums[i]
                lastidx += 1
        
        for i in range(lastidx + 1, n):
            nums[i] = 0
            
        