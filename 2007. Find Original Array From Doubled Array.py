class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2: return []
        count = Counter(changed)
        changed.sort()
        result = []
        for item in changed:
            if item == 0 and count[item] >= 2:
                count[item] -= 2
                result.append(item)
            elif item > 0 and count[item] and count[item*2]:
                count[item] -= 1
                count[item*2] -= 1
                result.append(item)
        if len(result) == len(changed) // 2:
            return result
        else:
            return []
