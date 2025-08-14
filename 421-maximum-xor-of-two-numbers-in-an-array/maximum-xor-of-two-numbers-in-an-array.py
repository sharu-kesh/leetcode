class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maxi = 0
        mask = 0
        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            s = set()
            for num in nums:
                s.add(num & mask)
            temp = maxi | (1 << i)
            for pre in s:
                if pre ^ temp in s:
                    maxi = temp
                    break
        return maxi