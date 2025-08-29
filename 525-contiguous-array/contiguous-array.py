class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, one = 0, 0
        res = 0

        mpp = {}

        for i, n in enumerate(nums):
            if n == 0: zero += 1
            else: one += 1

            if one - zero not in mpp:
                mpp[one - zero] = i
            
            if one == zero:
                res = one + zero
            else:
                idx = mpp[one - zero]
                res = max(res, i - idx)
        return res
        