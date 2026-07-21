class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        n = len(s)
        i = 0
        ans = ones

        while i < n and s[i] == '1':
            i += 1
        
        zeroFirst = 0
        while i < n and s[i] == '0':
            zeroFirst += 1
            i += 1
        
        while i < n:
            middleOne = 0
            while i < n and s[i] == '1':
                middleOne += 1
                i += 1
            
            if not middleOne: break
            zeroSecond = 0
            while i < n and s[i] == '0':
                zeroSecond += 1
                i += 1
            
            if not zeroSecond: break

            ans = max(ans, ones + zeroFirst + zeroSecond)
            zeroFirst = zeroSecond
        
        return ans
        