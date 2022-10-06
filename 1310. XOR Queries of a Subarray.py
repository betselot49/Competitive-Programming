class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        XOR = [0] * (len(arr) + 1)
        for i, num in enumerate(arr):
            XOR[i+1] = XOR[i] ^ num
        output = []
        for left, right in queries:
            output.append(XOR[left] ^ XOR[right + 1])
        return(output)
