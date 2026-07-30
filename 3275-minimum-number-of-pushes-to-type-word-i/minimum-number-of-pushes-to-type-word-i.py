class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        print(n)
        if n <= 8: return n
        elif n <= 16: return 8 + ((n - 8) * 2)
        elif n <= 24: return 24 + ((n - 16) * 3)
        return 24 + ((n - 16) * 3) + (n - 24)
        