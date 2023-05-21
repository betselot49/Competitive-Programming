class Solution(object):
    def accountsMerge(self, accounts):
        visited = [False] * len(accounts)
        accounts_map = defaultdict(list)
        res = []
    
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                accounts_map[email].append(i)
  
        def dfs(i, emails):
            if visited[i]:
                return
            visited[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbor in accounts_map[email]:
                    dfs(neighbor, emails)
       
        for i, account in enumerate(accounts):
            if visited[i]:
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res