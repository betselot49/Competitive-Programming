class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = []
        dDict = defaultdict(list)
        for path in paths:
            pathSplit = path.split(" ")
            root = pathSplit[0]
            for file in pathSplit[1:]:
                fileSplit = file.split("(")
                key = fileSplit[1][:-1]
                dDict[key].append(root + "/" + fileSplit[0])
        
        for value in dDict.values():
            if len(value) > 1:
                ans.append(value)
            
        return ans