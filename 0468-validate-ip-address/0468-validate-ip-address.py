class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def IPv4_checker(ipv4):
            try:
                for num in ipv4:
                    if str(int(num)) != num: return "Neither"
                    if int(num) < 0 or int(num) > 255: return "Neither" 
                    
                return "IPv4"
            except: return "Neither"
           

        def IPv6_checker(ipv6):
            for item in ipv6: 
                if len(item) == 0 or len(item) > 4: return "Neither"
                for i in item:
                    if '0' <= i <= '9' or 'a' <= i <= 'f' or "A" <= i <= "F": continue
                    return "Neither"
                
            return "IPv6"
        
        
        ipv4 = queryIP.split(".")
        if len(ipv4) == 4: 
            return IPv4_checker(ipv4)

        ipv6 = queryIP.split(":")
        if len(ipv6) == 8:
            return IPv6_checker(ipv6)

        return "Neither" 
        
   