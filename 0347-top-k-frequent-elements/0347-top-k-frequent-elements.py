class Solution(object):
    def topKFrequent(self, nums, k):
        counter_arr = Counter(nums).items()
        N = len(counter_arr)
        def quickSort(pivot, end, array, target):
            read = write = pivot + 1
            while read < end:
                if array[pivot][1] >= array[read][1]:
                    array[write], array[read] = array[read], array[write]
                    write += 1
                read += 1
            array[write-1], array[pivot] = array[pivot], array[write-1]
            if 0 <= len(counter_arr) - target - (write - 1) <= 1: return
            if len(counter_arr) - target < write - 1:
                quickSort(pivot, write-1, array, target)
            else:
                quickSort(write, end, array, target)
            
        quickSort(0, N, counter_arr, k)
        return [i[0] for i in counter_arr[N-k:]]

        