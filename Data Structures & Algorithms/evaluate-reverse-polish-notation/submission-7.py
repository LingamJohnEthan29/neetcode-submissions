class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens:
            if i not in '-+*/':
                stk.append(int(i))
            else:
                a = stk.pop()
                b = stk.pop()
                if i == '+':
                    stk.append(a+b)
                elif i == '-':
                    stk.append(b-a)
                elif i == '*':
                    stk.append(a*b)
                elif i == '/':
                    stk.append(int(b/a))
        return stk[-1]