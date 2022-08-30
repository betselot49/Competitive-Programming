class Solution:  
    def maxOperations(self, nums: List[int], k: int) -> int:
        output = 0
        counter = Counter(nums)
        checked = []
        for item in counter:
            if item == k/2:
                output += counter[item] // 2
            elif k - item in counter and k - item not in checked:
                output += min(counter[item], counter[k - item])
                checked.append(item)
        return output
