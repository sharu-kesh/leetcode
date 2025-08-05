class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s)
        l = 0
        count = 0
        ans = ''
        for i in range(n):
            if s[i] == '(':
                count += 1
            else:
                count -= 1
                if count == 0:
                    ans += s[l + 1: i]
                    l = i + 1
        return ans
        