class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.valid_ip = []
        def backtrack(ip_address, idx):
            if len(ip_address) == 4:  # If our ip_address collected enough ips: we don't need any more
                if idx == len(s):  # If we got valid Ips, we append it self.valid_ip
                    self.valid_ip.append(".".join(ip_address))
                return 
                
            for i in range(idx, len(s)):  
                curr = s[idx:i+1]  
                if len(curr) == len(str(int(curr))) and 0 <= int(curr) <= 255:  # if current is valid element of ip address, add to ip_address.
                    ip_address.append(curr)
                    backtrack(ip_address[:], i+1)
                    ip_address.pop()
                
        backtrack([], 0)
        return self.valid_ip