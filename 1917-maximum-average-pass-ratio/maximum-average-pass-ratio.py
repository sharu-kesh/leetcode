class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def profit(i, j):
            return (i + 1) / (j + 1) - i / j
        
        maxProfit = []

        for i, j in classes:
            heappush(maxProfit, (-profit(i, j), i, j))
        
        for e in range(extraStudents):
            val, i, j = heappop(maxProfit)
            heappush(maxProfit, (-profit(i + 1, j + 1), i + 1, j + 1))
        n = len(maxProfit)

        return sum(i / j for val, i, j in maxProfit) / n