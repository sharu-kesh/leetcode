class Solution:
    def canBeTypedWords(self, text: str, br: str) -> int:
        s = set(br)
        count = 0
        text = text.split()
        for word in text:
            flag = 0
            for i in word:
                if i in s:
                    flag = 1
                    break
                # print(i)
            if flag == 0: 
                count += 1
                # print(count)
        return count