class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        arr = []
        result = []
        if len(mat) * len(mat[0]) != r * c:
            return mat
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if len(arr) == c:
                    result.append(arr)
                    r -= 1
                    arr = []
                arr.append(mat[i][j])
        if len(arr) == c:
            result.append(arr)
        return result