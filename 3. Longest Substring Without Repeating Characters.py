class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        holder = []
        j = 0
        while j < len(s):
            i = j
            while i < len(s) and s[i] not in holder :
                holder.append(s[i])
                i += 1
            if len(holder) > length:
                length = len(holder)
            holder = []
            j += 1
            
        return length
