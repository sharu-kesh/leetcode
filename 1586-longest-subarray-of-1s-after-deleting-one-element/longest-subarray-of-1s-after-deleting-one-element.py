class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        resLen = 0
        count = 0
        n = len(nums)
        l = 0
        for r in range(n):
            if nums[r] == 0:
                count += 1
            while count > 1:
                if nums[l] == 0:
                    count -= 1
                l += 1
            resLen = max(resLen, r - l)
        return resLen 
        