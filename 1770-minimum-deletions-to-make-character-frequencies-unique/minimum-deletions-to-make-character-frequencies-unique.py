class Solution:
    def minDeletions(self, s: str) -> int:
        freq = [0] * 26
        for i in s:
            freq[ord(i) - ord('a')] += 1
        freq.sort(reverse = True)
        # idx = freq.index(0)
        # freq = freq[:idx]
        count = 0
        n = len(freq)
        # print(freq)
        for i in range(n):
            if not freq[i]: break
            for j in range(i + 1, n):
                if freq[i] != freq[j]:
                    break
                elif freq[j] <= 0: break
                freq[j] -= 1
                count += 1
        # print(freq)
        return count

        