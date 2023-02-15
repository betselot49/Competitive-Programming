class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ind1 = 0
        ind2 = 0
        merge = ""
        while ind1 < len(word1) and ind2 < len(word2):
            if word1[ind1:] > word2[ind2:]:
                merge += word1[ind1]
                ind1 += 1
            else:
                merge += word2[ind2]
                ind2 += 1
        merge += word1[ind1:] if ind1 < len(word1) else ""
        merge += word2[ind2:] if ind2 < len(word2) else ""
        
        return merge        