class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxi = max(nums)
        count = 0
        l = 0
        n = len(nums)
        res = 0
        for r in range(n):
            if nums[r] == maxi:
                count += 1
            
            while count >= k:
                if nums[l] == maxi:
                    count -= 1
                l += 1
            res += l
        return res