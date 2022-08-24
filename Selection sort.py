class Solution:
    def select(self, arr, i):
        position = i
        i += 1
        while i < len(arr):
            if arr[position] > arr[i]:
                position = i
            i += 1
        return position

    def selectionSort(self, arr, n):
        # code here
        i = 0
        while i < n:
            min = self.select(arr, i)
            arr[i], arr[min] = arr[min], arr[i]
            i += 1
        return arr
        
   # or
  
  def select(arr, i):
    minIndex = i
    for j in range(i + 1, len(arr)):
        if arr[minIndex] > arr[j]:
            minIndex = j
    return minIndex

def sort(n, arr):
    for i in range(n-1):
        minimum = select(arr, i)
        arr[i], arr[minimum] = arr[minimum], arr[i]
    print(arr)
