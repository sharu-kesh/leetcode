class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]
        n = len(s)
        for i in range(1, n):
            if stack and s[i].isupper() and stack[-1] == s[i].lower():
                stack.pop()
            elif stack and stack[-1].isupper() and stack[-1].lower() == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack)
        