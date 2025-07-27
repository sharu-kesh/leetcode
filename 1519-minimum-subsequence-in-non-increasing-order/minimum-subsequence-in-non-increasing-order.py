class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        sumi = sum(nums)
        res = []
        count = 0
        i = 0
        while count <= sumi:
            res.append(nums[i])
            sumi -= nums[i]
            count += nums[i]
            i += 1
        return res

        