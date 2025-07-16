class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd = even = 0
        for num in nums:
            if num & 1: odd += 1
            else: even += 1
        even_dp = odd_dp = 0
        for num in nums:
            if num & 1:
                odd_dp = max(odd_dp, even_dp + 1)
            else:
                even_dp = max(even_dp, odd_dp + 1) 
        return max(odd, even, odd_dp, even_dp)
