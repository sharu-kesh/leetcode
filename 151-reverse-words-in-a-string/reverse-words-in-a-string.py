import re
class Solution:
    def reverseWords(self, s: str) -> str:
        # s = re.sub(' +', ' ', s)
        # print(s)
        s = list(s.split())
        return ' '.join(s[::-1])