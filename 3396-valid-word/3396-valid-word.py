class Solution:
    def isValid(self, word: str) -> bool:
        consonants = 'bcdfghjklmnpqrstvwxyz'
        vowels = 'aeiou'
        digits = '1234567890'
        chars = cons = vow = 0
        for i in word:
            if i.lower() in consonants:
                cons += 1
                chars += 1
            elif i.lower() in vowels:
                vow += 1
                chars += 1
            elif i.isdigit():
                chars += 1
            else: return False
        return chars >=3 and vow >= 1 and cons >= 1 
        