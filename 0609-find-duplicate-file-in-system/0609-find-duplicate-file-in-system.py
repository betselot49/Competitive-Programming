class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        """
        
        ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
        
    
        first = root/a 1.txt(abcd) 2.txt(efgh)
        
        first.split(" ") =>  [root/a,    1.txt(abcd),    2.txt(efgh)]   
        
        root = first[0]
        
        file1 = 1.txt(abcd)
        
        fileSplit = file1.split("(") = 1.text,  abcd)
        
        key = fileSplit[-1][:-1]
        
        difaultDict[key].append(root + / + fileSplit[0])
        """
        
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