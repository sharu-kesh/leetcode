class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mpp = {}
        for a, b in zip(s, t):
            if a not in mpp:
                for key, val in mpp.items():
                    if val == b:
                        return False
                mpp[a] = b
            elif mpp[a] != b:
                return False
        return True
        