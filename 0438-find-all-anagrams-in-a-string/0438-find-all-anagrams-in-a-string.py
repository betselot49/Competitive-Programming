class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter(p)
        left = 0
        ans = []
        compare = defaultdict(int)
        for right, num in enumerate(s):
            compare[s[right]] += 1
            if right - left + 1 == len(p):
                if compare == count:
                    ans.append(left)
                compare[s[left]] -= 1
                if compare[s[left]] == 0:
                    del compare[s[left]]
                left += 1
            
        return ans
                
        
            
                
