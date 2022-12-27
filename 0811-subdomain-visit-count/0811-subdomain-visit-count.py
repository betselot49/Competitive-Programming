class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = []
        demoDict = defaultdict(int)
    
        for cpdomain in cpdomains:
            cpdomain = cpdomain.split(" ")
            num, domain = int(cpdomain[0]), cpdomain[1].split(".")
        
            for i in range(len(domain)):
                key = ".".join(domain[i:])
                demoDict[key] += num
    
        for key, value in demoDict.items():
            ans.append(str(value) + " " + key)
        
        return ans