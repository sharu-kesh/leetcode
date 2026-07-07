class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sumi = 0
        cur = 0
        stack = []
        while n:
            val = n % 10
            if val:
                stack.append(val)
                sumi += val
            n = n // 10
        while stack:
            cur = (cur * 10) + stack.pop()
        return cur * sumi