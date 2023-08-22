class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        limit = int(area ** 0.5)
        for i in range(limit, 0, -1):
            if area % i == 0:
                return [area//i, i]