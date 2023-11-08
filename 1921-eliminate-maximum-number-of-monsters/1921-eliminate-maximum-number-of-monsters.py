class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        times = sorted([d/s for d, s in zip(dist, speed)])
        for i, time in enumerate(times):
            if i >= time: return i
        
        return len(times)