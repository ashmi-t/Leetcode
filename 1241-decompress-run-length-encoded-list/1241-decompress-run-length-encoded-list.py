class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(0,len(nums),2):
            arr+=[nums[i+1]]*nums[i]
        return arr

