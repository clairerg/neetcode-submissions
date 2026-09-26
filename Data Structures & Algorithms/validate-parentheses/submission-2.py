class Solution:
    def isValid(self, s: str) -> bool:
        matching = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in matching:
                stack.append(c)
            else:
                if not stack:
                    return False
                if c == matching[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
            


        