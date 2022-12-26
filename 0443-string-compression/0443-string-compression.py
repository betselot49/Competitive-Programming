class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0
        while j < len(chars):
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
            if j - i > 1:
                count = str(j - i)
                for c in count:
                    chars[i+1] = c
                    i += 1
            while j - 1 != i:
                chars.pop(j-1)
                j -= 1
            i = j
        return len(chars)

