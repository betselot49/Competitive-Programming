# User function Template for python3

class Solution:
    def selectionSort(self, arr, n):
        # code here
        for holder in range(n):
            minIndex = holder
            for seeker in range(holder, n):
                if arr[seeker] < arr[minIndex]:
                    minIndex = seeker
            arr[holder], arr[minIndex] = arr[minIndex], arr[holder]
        return arr
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
