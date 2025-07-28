class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        val = 0
        n = len(nums)
        for i in nums:
            val |= i
        count = 0
        def f(index,curOr):
            nonlocal count, n, val
            if curOr == val:
                count += 1
            for i in range(index, n):
                f(i + 1, curOr | nums[i])

        f(0, 0)
        return count