from math import gcd
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        
        def lcm(a, b):
            return (a * b) // gcd(a, b)
        stack = [nums[0]]
        n = len(nums)

        for i in range(1, n):
            stack.append(nums[i])
            while len(stack) > 1 and gcd(stack[-1], stack[-2]) > 1:
                a = stack.pop()
                b = stack.pop()
                stack.append(lcm(a, b))
        return stack