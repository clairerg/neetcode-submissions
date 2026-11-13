class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':        
                a = stack.pop()
                b = stack.pop()
                ans = 0
                if token == '+':
                    ans += a + b
                elif token == '-':
                    ans += b - a
                elif token == '*':
                    ans += a * b
                else:
                    ans += int(b/a)
                stack.append(ans)
            else:
                stack.append(int(token))
        
        return stack[-1]
