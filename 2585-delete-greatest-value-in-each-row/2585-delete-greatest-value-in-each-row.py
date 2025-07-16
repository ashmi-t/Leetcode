class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in range(0,len(grid)):
            grid[i].sort(reverse=True)    
        sum =0
        temp_max=0
        for j in range(0,len(grid[i])):
            for k in grid:
                temp_max=max(temp_max,k[0])
                k.pop(0)
            sum+= temp_max
            temp_max=0
        return sum



