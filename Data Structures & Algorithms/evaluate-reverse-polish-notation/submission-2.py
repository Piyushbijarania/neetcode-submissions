class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            stack.append(c)
            if stack[-1] in ["+", "-", "*", "/"]:
                operator = stack.pop()
                b = int(stack.pop())
                a = int(stack.pop())
                result = 0
                if operator == "+":
                    result = a + b
                elif operator == "-":
                    result = a - b
                elif operator == "*":
                    result = a * b
                else:
                    result = int(a / b)
                stack.append(str(result))
        return int(stack[-1])
        