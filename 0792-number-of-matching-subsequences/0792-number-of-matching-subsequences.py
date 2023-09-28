class Solution:        
    def binarySearch(self, target, arr):
        if len(arr) == 0: return -1

        left, right =-1, len(arr)
        while left + 1 < right:
            mid = left + (right - left) // 2
            if arr[mid] >= target:
                right = mid
            else:
                left = mid

        if right >= len(arr):
            return -1
        else:
            return arr[right]
        
        
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dic = defaultdict(list)
        for i, char in enumerate(s):
            dic[char].append(i)
        
        ans = 0
        for word in words:
            idx, count = 0, 0
            for i, char in enumerate(word):   
                found = self.binarySearch(idx, dic[char])
                if found == -1:
                    break
                else:
                    count += 1
                    idx = found + 1
                    
            if count == len(word):
                ans += 1
                
        return ans
                    
     