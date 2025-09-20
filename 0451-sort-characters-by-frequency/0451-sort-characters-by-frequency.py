class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for c in s:
            freq[c] = 1 + freq.get(c, 0)

        freq = sorted(freq.items(), key=lambda x: -x[1])

        return ''.join([key * val for key, val in freq])