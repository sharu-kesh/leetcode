class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def findSubArray(k):
            if k <= 0: return 0
            freq = defaultdict(int)
            l = 0
            count = 0
            res = 0
            for r in range(len(nums)):
                if not freq[nums[r]]: count += 1
                freq[nums[r]] += 1
                while count > k:
                    freq[nums[l]] -= 1
                    if not freq[nums[l]]:
                        del freq[nums[l]]
                        count -= 1
                    l += 1
                res += r - l + 1
            return res
        return findSubArray(k) - findSubArray(k - 1)
        