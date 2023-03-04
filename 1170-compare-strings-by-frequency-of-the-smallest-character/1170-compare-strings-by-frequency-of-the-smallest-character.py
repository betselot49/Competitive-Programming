class Solution:
    def helper(self, queries):
        query_fre = []
        for query in queries:
            query = sorted(query)
            mini = query[0]
            counter = Counter(query)
            query_fre.append(counter[mini])
        return query_fre
    
    def binarySearch(self, array, target):
        low = -1
        high = len(array)
        
        while low + 1 < high:
            mid = low + (high - low) // 2
            if array[mid] <= target:
                low = mid
            else:
                high = mid
                
        return high
            
    
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        queries = self.helper(queries)
        words = self.helper(words)
        words.sort()
        
        count = []
        for query in queries:
            index = self.binarySearch(words, query)
            count.append(len(words) - index)
                
        return count
            
            
        
        
        