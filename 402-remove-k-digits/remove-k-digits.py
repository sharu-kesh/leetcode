class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k: return '0'
        stack = []
        for i in num:
            while stack and stack[-1] > i and k:
                stack.pop()
                k -= 1
            stack.append(i)
        stack = stack[:len(stack) - k]
        return ''.join(stack).lstrip('0') or '0'
        