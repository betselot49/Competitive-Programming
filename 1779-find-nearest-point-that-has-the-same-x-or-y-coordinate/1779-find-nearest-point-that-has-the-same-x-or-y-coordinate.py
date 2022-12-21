class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minDist = -1
        minIndex = -1
        for i, point in enumerate(points):
            if x == point[0] or y == point[1]:
                manDist = abs(x-point[0]) + abs(y-point[1])
                if minDist == -1 or manDist < minDist:
                    minDist = manDist
                    minIndex = i
        return minIndex
                