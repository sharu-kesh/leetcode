class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i, j, time in roads:
            adj[i].append((j, time))
            adj[j].append((i, time))
        dist = [float('inf')] * n
        dist[0] = 0
        ways = [0] * n
        ways[0] = 1
        minH = [(0, 0)]
        mod = 10**9 +7
        while minH:
            prev_time, curNode = heappop(minH) 
            for nei, time in adj[curNode]:
                new_time = prev_time + time
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    ways[nei] = (ways[curNode]) % mod
                    heappush(minH, (new_time, nei))
                elif new_time == dist[nei]:
                    ways[nei] = (ways[curNode] + ways[nei]) %mod
        return ways[-1] % mod