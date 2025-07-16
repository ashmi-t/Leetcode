class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        arr=[]
        for i in sentences:
            arr.append(len(i.split(" ")))
        return max(arr)    
            