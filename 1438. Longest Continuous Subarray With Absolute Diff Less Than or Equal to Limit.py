class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQ = collections.deque()
        maxQ = collections.deque()
        output, i = 0, 0
        for j, num in enumerate(nums):
            while len(minQ) > 0 and num > minQ[-1]:
                minQ.pop()
            minQ.append(num)
            
            while len(maxQ) > 0 and num < maxQ[-1]:
                maxQ.pop()
            maxQ.append(num)
            
            while minQ[0] - maxQ[0] > limit:
                if minQ[0] == nums[i]:
                    minQ.popleft()
                if maxQ[0] == nums[i]:
                    maxQ.popleft()
                i += 1
            output = max(output, j - i + 1)
        return output 
                      
