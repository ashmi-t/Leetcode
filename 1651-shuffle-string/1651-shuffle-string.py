class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        x = " "*(len(indices))
        for i in range(0,len(indices)):
            x= x[:indices[i]]+s[i]+x[indices[i]+1:]
        return x
