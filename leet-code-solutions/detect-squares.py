class DetectSquares(object):

    def __init__(self):
        self.plane = defaultdict(int)
        
    def add(self, point):
        x, y = point
        self.plane[(x, y)] += 1

    def count(self, point):
        p1, p2 = point
        squares = 0
        for x, y in list(self.plane.keys()):
            if (p1, p2) == (x, y): continue
            
            if p1 + p2 == x + y or x - y == p1 - p2:
                squares += self.plane[(x, y)] * self.plane[(x, p2)] * self.plane[(p1, y)]
                
        return squares

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)