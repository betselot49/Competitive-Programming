class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        output = 0
        count = Counter(arr)

        for i, x in count.items():
            for j, y in count.items():
                k = target - i - j
                if k not in count:
                    continue
                if i == j == k:
                    output = (output + x * (x - 1) * (x - 2) // 6) % 1_000_000_007
                elif i == j and j != k:
                    output = (output + x * (x - 1) // 2 * count[k]) % 1_000_000_007
                elif i < j < k:
                    output = (output + x * y * count[k]) % 1_000_000_007

        return output % 1_000_000_007
