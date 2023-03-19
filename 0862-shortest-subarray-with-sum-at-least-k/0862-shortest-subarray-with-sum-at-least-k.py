class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue = deque([[0,0]])
        min_length = float("inf")
        curr_sum = 0
        
        for idx, num in enumerate(nums):
            curr_sum += num
            
            while queue and curr_sum - queue[0][1] >= k:
                min_length = min(min_length, idx+1 - queue.popleft()[0])
                
            while queue and curr_sum <= queue[-1][1]:
                queue.pop()
            queue.append([idx+1, curr_sum])
        return -1 if min_length == float("inf") else min_length