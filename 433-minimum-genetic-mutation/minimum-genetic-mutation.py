class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        s = set(bank)
        if end not in s and start != end: return -1
        q = deque([(start, 0)])
        vis = {start}
        while q:
            g, d = q.popleft()
            if g == end: return d
            for i in range(8):
                for c in 'ACGT':
                    if g[i] != c:
                        n = g[:i] + c + g[i + 1:]
                        if n in s and n not in vis:
                            vis.add(n)
                            q.append((n, d + 1))
        return -1
