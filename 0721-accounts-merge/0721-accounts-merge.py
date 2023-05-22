class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # every account is the rep of it self
        root = { acc: acc for account in accounts for acc in account[1:] }
        size = { acc: 1 for account in accounts for acc in account[1:] }
        group = { acc : account[0] for account in accounts for acc in account[1:] }
        account_dec = defaultdict(set)
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            
            if rootX != rootY:
                if size[rootX] < size[rootY]:
                    root[rootX] = rootY
                    size[rootY] += size[rootX]
                else:
                    root[rootY] = rootX
                    size[rootX] += size[rootY]
            
        def find(x):
            rootX = root[x]
            while rootX != root[rootX]:
                rootX = root[rootX]
                
            while x != rootX:
                parent = root[x]
                root[x] = rootX
                x = parent
            
            return rootX
        
        # union each account with each other
        for account in accounts:
            for i in range(1, len(account)-1):
                for j in range(i+1, len(account)):
                    union(account[i], account[j])
                    
        # for each account find its root account and add into their represenatatives set
        for account in accounts:
            for i in range(1, len(account)):
                account_dec[find(account[i])].add(account[i])
        
        # collect each accounts (sorted) from their representatives and append to answer with their owner name
        answer = []    
        for key, value in list(account_dec.items()):
            temp = [group[key]]
            temp += sorted(list(value))
            answer.append(temp)            
            
            
        return answer
                
        
                