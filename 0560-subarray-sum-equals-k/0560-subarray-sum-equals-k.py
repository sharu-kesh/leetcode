class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        di = defaultdict(int)
        sumi = 0
        count = 0
        for i in nums:
            sumi += i
            if sumi == k:
                count += 1
            count += di[sumi - k]
            di[sumi] += 1
        return count