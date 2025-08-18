class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)

        def check(num):
            res = 0
            for i in nums:
                res += ceil(i / num)
            return res <= threshold
        ans  = 0
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
        