class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t[-1].isdigit():
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                res = 0
                if t == '+':
                    res = a + b                    
                elif t == '-':
                    res = a - b
                elif t == '*':
                    res = a * b
                elif t == '/':
                    res = int(a / b)
                    #print(res,a,b)
                stack.append(res)
        return stack.pop()
        