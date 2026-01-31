class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        maxi = 26
        val = ord(target)
        for i in letters:
            if i <= target: continue
            diff = ord(i) - val
            maxi = min(maxi, diff)
        
        if maxi == 26: return letters[0]
        return chr(val + maxi)
        