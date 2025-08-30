class Solution:
    def decodeString(self, s: str) -> str:
        res = ''
        stack = []
        for i in s:
            if i == ']':
                temp = []
                while stack and not stack[-1].isdigit():
                    temp.append(stack.pop())
                temp.pop()
                count = ''
                while stack and stack[-1].isdigit():
                    count += stack.pop()
                print(count)
                temp = ''.join(temp[::-1])
                stack.append(int(count[::-1]) * temp)
            
            else:
                stack.append(i)
        return ''.join(stack)

        