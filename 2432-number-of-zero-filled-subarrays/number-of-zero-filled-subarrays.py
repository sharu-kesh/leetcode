class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        res = 0
        for i in range(n):
            if nums[i] == 0:
                count += 1
            elif count >= 1:
                res += (count * (count + 1)) // 2
                count = 0
        if count:
            res += (count * (count + 1)) // 2
        return res
        