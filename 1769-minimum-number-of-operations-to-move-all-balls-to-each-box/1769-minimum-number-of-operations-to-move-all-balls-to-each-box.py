class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        length = len(boxes)
        minMoves = [0] * length
        
        for index, box in enumerate(boxes):
            if int(box):
                for placer in range(len(boxes)):
                    minMoves[placer] += abs(index - placer)
                    
        return minMoves