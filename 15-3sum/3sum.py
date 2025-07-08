class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            j = i + 1
            k = n - 1
            if i > 0 and nums[i] == nums[i - 1]: continue
            while j < k:
                sume = nums[i] + nums[j] + nums[k]
                if sume == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]: j += 1
                    while j < k and nums[k] == nums[k + 1]: k -= 1
                elif sume < 0:
                    j += 1
                else:
                    k -= 1
        return res

        