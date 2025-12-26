class Solution:
    def bestClosingTime(self, cust: str) -> int:
        m = len(cust)
        j = 0
        penalty = 0
        pre = 0
        for i in range(m):
            pre += -1 if cust[i] == 'Y' else 1

            if pre < penalty:
                j = i + 1
                penalty = pre
            
        return j





        