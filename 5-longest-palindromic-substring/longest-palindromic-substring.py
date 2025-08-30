class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        leng=0
        n=len(s)
        for i in range(n):
            l=r=i
            while l>=0 and r<n and s[l]==s[r]:
                if r-l+1 > leng:
                    res=s[l:r+1]
                    leng=r-l+1
                l-=1
                r+=1
            l,r=i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                if r-l+1 > leng:
                    res=s[l:r+1]
                    leng=r-l+1
                l-=1
                r+=1
        return res
        