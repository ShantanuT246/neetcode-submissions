class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_integer(text):
            try:
                int(text)
                return True
            except ValueError:
                return False

        stack = []
        for i in tokens:
            if is_integer(i):
                stack.append(int(i))
                continue
            if i == "+":
                result = stack.pop() + stack.pop()

            elif i == "*":
                result = stack.pop() * stack.pop()

            elif i == "-":
                b = stack.pop()
                a = stack.pop()
                result = a - b

            else: 
                b = stack.pop()
                a = stack.pop()
                result = int(a / b)

            stack.append(result)

        return stack[0]
            