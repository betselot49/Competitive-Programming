class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashT = defaultdict(list)
        
        for item in strs:    
            hashT["".join(sorted(item))].append(item)
        
        ans = []
        for value in hashT.values():
            ans.append(value)
            
        return ans
            