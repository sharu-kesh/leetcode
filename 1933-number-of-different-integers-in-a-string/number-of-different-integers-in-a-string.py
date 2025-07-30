class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        pre = ''
        s = set()
        for i in word:
            if not i.isdigit():
                if pre: s.add(int(pre))
                pre = ''
            else:
                pre += i
        if pre: s.add(int(pre))
        return len(s)