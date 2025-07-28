class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * (n + 1)
        dist[0] = 0
        dist[k] = 0
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        minH = [(0, k)]
        while minH:
            prev_weight, curNode = heappop(minH)
            for nei, weight in adj[curNode]:
                new_weight = prev_weight + weight
                if new_weight < dist[nei]:
                    dist[nei] = new_weight
                    heappush(minH, (new_weight, nei))
        if max(dist) != float('inf'):
            return max(dist)
        return -1
        