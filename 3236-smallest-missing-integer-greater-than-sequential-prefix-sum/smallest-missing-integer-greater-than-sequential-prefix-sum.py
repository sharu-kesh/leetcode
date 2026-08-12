class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        sumi = nums[0]
        seen = set(nums)

        for i in range(1, n):
            if nums[i] - 1 == nums[i - 1]:
                sumi += nums[i]
            else: break
        
        while sumi in seen:
            sumi += 1
        return sumi
        