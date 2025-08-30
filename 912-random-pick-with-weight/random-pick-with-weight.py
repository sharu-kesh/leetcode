class Solution:

    def __init__(self, w: List[int]):
        self.pre = []
        tot = 0
        for i in w:
            tot += i
            self.pre.append(tot)
        self.tot = tot

    def pickIndex(self) -> int:
        rand = random.randint(1, self.tot)
        return bisect.bisect_left(self.pre, rand)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()