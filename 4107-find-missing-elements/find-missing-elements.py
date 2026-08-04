class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini, maxi = min(nums), max(nums)
        res = []
        nums.sort()
        i = mini
        j = 0
        while i <= maxi:
            if i != nums[j]:
                res.append(i)
            else: j += 1
            i += 1
        return res