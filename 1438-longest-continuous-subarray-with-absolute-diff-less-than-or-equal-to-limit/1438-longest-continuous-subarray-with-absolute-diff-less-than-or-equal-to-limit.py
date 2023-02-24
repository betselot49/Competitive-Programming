class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc_dequeue = deque()
        dec_dequeue = deque()
        length = left = 0
        
        for right, num in enumerate(nums):
            while inc_dequeue and inc_dequeue[-1] > nums[right]:
                inc_dequeue.pop()
            inc_dequeue.append(num)
            
            while dec_dequeue and dec_dequeue[-1] < nums[right]:
                dec_dequeue.pop()
            dec_dequeue.append(num)
            
            while dec_dequeue[0] - inc_dequeue[0] > limit:
                if dec_dequeue[0] == nums[left]:
                    dec_dequeue.popleft()
                elif inc_dequeue[0] == nums[left]:
                    inc_dequeue.popleft()
                left += 1

            length = max(length, right - left + 1)    
            
        return length
            