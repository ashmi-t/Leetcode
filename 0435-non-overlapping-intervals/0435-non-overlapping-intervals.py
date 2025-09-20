class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count=0
        prevSt=intervals[-1][0]
        n=len(intervals)
        for j in range(n-2,-1,-1):
            if intervals[j][1]<=prevSt:
                prevSt=intervals[j][0]  
            else:
                count+=1
        return count