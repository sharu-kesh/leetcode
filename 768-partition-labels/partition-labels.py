class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = {}
        for i, val in enumerate(s):
            freq[val] = i
        
        size = 0
        end = 0
        res = []
        for i, val in enumerate(s):
            size += 1
            if freq[val] > end:
                end = freq[val]
            if i == end:
                res.append(size)
                size = 0
        return res