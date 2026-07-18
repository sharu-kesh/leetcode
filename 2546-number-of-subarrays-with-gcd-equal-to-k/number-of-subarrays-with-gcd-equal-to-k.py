class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if b > a: a, b = b, a

            while b != 0:
                a, b = b, a % b
            return a
        
        count = 0

        n = len(nums)
        for i in range(n):
            val = nums[i]
            if val == k: count += 1
            for j in range(i + 1, n):
                val = gcd(val, nums[j])
                if val == k:
                    count += 1
        return count
        