class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        arr = []
        for i in range(0,len(index)):
            arr.insert(index[i],nums[i])
        return arr