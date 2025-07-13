class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        freq = Counter(t)
        required = len(freq)
        formed = 0
        window_counts = {}
        minLength = float('inf')
        start = -1
        l = 0
        
        for r in range(n):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            if char in freq and window_counts[char] == freq[char]:
                formed += 1
            
            while formed == required:
                if r - l + 1 < minLength:
                    minLength = r - l + 1
                    start = l
                
                window_counts[s[l]] -= 1
                if s[l] in freq and window_counts[s[l]] < freq[s[l]]:
                    formed -= 1
                l += 1
        
        return s[start: start + minLength] if start != -1 else ''