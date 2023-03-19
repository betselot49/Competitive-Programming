class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len_t = len(t)
        dic_t = Counter(t)
        left = count = right = 0
        window = defaultdict(int)
        ans = ""
        
        for right, char in enumerate(s):
            if char in dic_t:
                window[char] += 1
                if window[char] <= dic_t[char]:
                    count += 1
                    
            while count == len_t:
                if not ans or right - left + 1 < len(ans):
                    ans = s[left : right + 1]
                curr = s[left]
                if curr in dic_t:
                    window[curr]  -= 1
                    if window[curr] < dic_t[curr]:
                        count -= 1  
                left += 1
                
        return ans
                