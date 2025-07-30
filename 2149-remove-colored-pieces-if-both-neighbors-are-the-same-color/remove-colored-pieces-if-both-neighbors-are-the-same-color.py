class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        A = B = 0
        stack = []
        for i in colors:
            stack.append(i)
            while len(stack) > 2 and stack[-2] ==  stack[-1] == stack[-3]:
                removed = stack.pop()
                if removed == 'A': A += 1
                else: B += 1
        print(A, B)
        if (A == 0 and B == 0 ) or A <= B: return False
        return True
        