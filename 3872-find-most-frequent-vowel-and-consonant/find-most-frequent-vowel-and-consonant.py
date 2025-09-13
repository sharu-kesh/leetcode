class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a','e','i','o','u'}
        vow = cons = 0
        freq = Counter(s)
        for key, val in freq.items():
            if key in vowels:
                vow = max(vow, val)
            else:
                cons = max(cons, val)
        return vow + cons