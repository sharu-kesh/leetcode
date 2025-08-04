class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = defaultdict(int)
        l = 0
        maxLen = 0
        n = len(fruits)
        distinct = 0
        for r in range(n):
            if not freq[fruits[r]]: distinct += 1
            freq[fruits[r]] += 1
            while distinct > 2:
                freq[fruits[l]] -= 1
                if not freq[fruits[l]]: 
                    del freq[fruits[l]]
                    distinct -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen
        