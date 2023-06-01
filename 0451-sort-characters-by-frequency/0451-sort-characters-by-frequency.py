class Solution:
    def frequencySort(self, s: str) -> str:
        freq= Counter(s)
        z=sorted(freq.items(), key=lambda x:-x[1])
        ans=''
        for i in range(len(z)):
            ans+=z[i][0]*z[i][1]
            
        return ans