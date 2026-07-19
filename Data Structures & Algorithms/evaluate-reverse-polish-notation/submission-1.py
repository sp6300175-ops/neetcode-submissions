class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
            if i == '+':
                a = stack.pop()
                b = stack.pop()
                res = a + b
                stack.append(res)
            elif i == '*':
                a = stack.pop()
                b = stack.pop()
                res = a * b
                stack.append(res)
            elif i == '-':
                a = stack.pop()
                b = stack.pop()
                res = b - a
                stack.append(res)
            elif i == '/':
                a = stack.pop()
                b = stack.pop()
                res = int(b / a)
                stack.append(res)
        return stack[0]