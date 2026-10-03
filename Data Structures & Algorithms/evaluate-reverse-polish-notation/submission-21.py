class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-*/":
                a = stack.pop()   # right operand
                b = stack.pop()   # left operand
                if t == "+":
                    stack.append(b + a)
                elif t == "-":
                    stack.append(b - a)
                elif t == "*":
                    stack.append(b * a)
                else:
                    stack.append(int(b / a))  # truncate toward zero
            else:
                stack.append(int(t))
        return stack[-1]