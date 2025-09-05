class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b, c = 0, 0
        freq = Counter(secret)
        count = 0
        for i in guess:
            if i in freq and freq[i] > 0:
                count += 1
                freq[i] -= 1
        for i, j in zip(guess, secret):
            if i == j: b += 1
        c = count - b
        return f'{b}A{c}B'
        