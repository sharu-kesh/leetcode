class Solution:
    def makeFancyString(self, s: str) -> str:
        prev = s[0]
        count = 1
        for i in range(1, len(s)):
            if prev[-1] == s[i]:
                count += 1
                if count == 3:
                    count -= 1
                else:
                    prev += s[i]
            else:
                count = 1
                prev += s[i]
        return prev