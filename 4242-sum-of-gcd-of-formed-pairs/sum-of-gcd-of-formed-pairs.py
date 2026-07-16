class Solution:
    def gcd(self, a, b):
        if b > a: a, b = b, a
        while b != 0:
            a, b = b, a % b
        return a

    def gcdSum(self, nums: list[int]) -> int:
        pre = [nums[0]]
        maxi = nums[0]
        n = len(nums)
        for i in range(1, n):
            maxi = max(maxi, nums[i])
            pre.append(self.gcd(maxi, nums[i]))
        pre.sort()
        l = 0
        r = len(pre) - 1
        sumi = 0
        while l < r:
            sumi += self.gcd(pre[l], pre[r])
            l += 1
            r -= 1
        return sumi
