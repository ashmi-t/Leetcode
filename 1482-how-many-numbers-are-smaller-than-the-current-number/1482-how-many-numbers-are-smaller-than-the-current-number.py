class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr =[]
        count = 0
        for i in nums:
            for j in nums:
                if i!=j and j<i:
                    count += 1  
            arr.append(count)
            count=0
        return arr

