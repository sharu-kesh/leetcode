class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True
        pre = nums[0]
        inc = dec = 0
        for i in range(1, n):
            if nums[i] - pre > 0:
                inc += 1
            elif nums[i] - pre < 0:
                dec += 1
            pre = nums[i]
        if (inc and not dec) or (not inc and dec) or (not inc and not dec):
            return True
        return False

        