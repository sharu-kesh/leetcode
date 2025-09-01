class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [(i, j) for i, j in zip(capital, profits)]
        projects.sort()
        maxH = []
        i = 0
        n = len(projects)
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heappush(maxH, -projects[i][1])
                i += 1
            if not maxH:
                break
            w -= heappop(maxH)
        return w
