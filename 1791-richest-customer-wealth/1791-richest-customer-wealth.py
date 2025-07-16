class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        arr = 0
        for i in range(0,len(accounts)):
           arr= max(sum(accounts[i]),arr)
        return arr