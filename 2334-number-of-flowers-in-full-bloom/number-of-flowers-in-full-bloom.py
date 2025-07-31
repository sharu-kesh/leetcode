class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        res = [0] * len(people)
        people = [(p, i) for i, p in enumerate(people)]
        minH = []
        flowers.sort()
        j = 0
        for p, i in sorted(people):
            while j < len(flowers) and flowers[j][0] <= p:
                heappush(minH, flowers[j][1])
                j += 1
            while minH and minH[0] < p:
                heappop(minH)
            res[i] = len(minH)
        return res