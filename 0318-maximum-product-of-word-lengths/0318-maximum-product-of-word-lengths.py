class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bits = []
        for word in words:
            word_to_num = 0
            for char in word:
                word_to_num |= 2 ** (ord(char) - 97)
            bits.append([word_to_num, len(word)])
            
        maxLength = 0
        for idx, bit in enumerate(bits):
            for j in range(idx+1, len(bits)):
                if bits[j][0] & bit[0] == 0:
                    maxLength = max(maxLength, bit[1] * bits[j][1])
        return maxLength
        