class Solution:
    def frequencySort(self, s: str) -> str:
        freq = sorted(Counter(s).items(), key = lambda x : x[1], reverse = True)
        s = ''
        for val, times in freq:
            s += val * times
        return s
        