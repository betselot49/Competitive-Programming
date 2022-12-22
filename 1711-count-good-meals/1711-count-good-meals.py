class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        twoPower = set()
        for i in range(22):
            twoPower.add(2 ** i)
        seen = defaultdict(int)
 
        ans = 0           
        for food in deliciousness:
            for item in twoPower:
                if item - food in seen:
                    ans += seen[item - food]
                    ans = ans % ((10 ** 9) + 7)
            seen[food] += 1
            
        return ans   
        