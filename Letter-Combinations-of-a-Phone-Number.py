from itertools import product
class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        result = []
        num = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        for i in digits:
            if i in num:
                result.append(num[i])

        if not result or any(len(group) == 0 for group in result):
            return []
        else:
            result = [''.join(p) for p in product(*result)]
        return result
        