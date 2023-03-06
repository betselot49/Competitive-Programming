class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        N = len(nums)
        request_list = [0] * N
        result = 0
        MOD = 10 ** 9 + 7
        
        for request in requests:
            request_list[request[0]] += 1
            if request[1]+1 < N:
                request_list[request[1]+1] -= 1
            
            
        # prefix sum claculation
        for ind in range(1, N):
            request_list[ind] += request_list[ind-1]
        
        nums.sort(reverse = True)
        request_list.sort(reverse = True)
        
        for index, num in enumerate(request_list):
            result += num * nums[index]
            
        return result % MOD
        
        
        