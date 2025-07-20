class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = []
        freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
        for key, val in freq.items():
            res.append(key)
            if len(res) == k: break
        return res