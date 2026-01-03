import operator

class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
        pastExpr = {}
        def compute(expr):
            if expr.isdigit():
                return [int(expr)]
            if expr in pastExpr:
                return pastExpr[expr]
            ans = []
            for i, ch in enumerate(expr):
                if ch in ops:
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])
                    for a in left:
                        for b in right:
                            ans.append(ops[ch](a, b))
            pastExpr[expr] = ans
            return ans
        return compute(expression)