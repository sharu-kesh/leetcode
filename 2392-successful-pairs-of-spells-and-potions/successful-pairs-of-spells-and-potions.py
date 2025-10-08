class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        m = len(potions)
        for i in spells:
            req_strength = math.ceil(success / i)
            if req_strength > potions[-1]:
                ans.append(0)
                continue
            idx = bisect_left(potions, req_strength)
            ans.append(m - idx)
        return ans
