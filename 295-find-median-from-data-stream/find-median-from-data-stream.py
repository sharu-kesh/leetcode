class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heappush(self.small, -num)

        if self.small and self.large and -1 * self.small[0] > self.large[0]:
            val = -1 * heappop(self.small)
            heappush(self.large, val)
        
        if len(self.small) > len(self.large) + 1:
            val = -1 * heappop(self.small)
            heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heappop(self.large)
            heappush(self.small, -1 * val)
        
    def findMedian(self) -> float:
        n = len(self.small)
        m = len(self.large)
        tot = n + m
        if tot & 1:
            if n > m:
                return -1 * self.small[0]
            else:
                return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()