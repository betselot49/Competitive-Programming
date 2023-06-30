class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:        
        def mergeSort(array):
            if len(array) == 0: return array
            if len(array) == 1: return [[array[0], 0, 0]]
            
            mid = len(array) // 2
            left = mergeSort(array[:mid])
            right = mergeSort(array[mid:])
            
            return merge(left, right)
        
        def merge(left, right):
            idx1 = idx2 = 0
            merged = []
            # Count the number of numbers less than end greater than itself and store in the form of [number, lessThan, greaterThan] only from the left array
            while idx1 < len(left) and idx2 < len(right):
                if left[idx1][0] == right[idx2][0]:
                    curr = left[idx1][0]
                    left_ptr = idx1
                    while idx1 < len(left) and left[idx1][0] == curr:
                        merged.append(left[idx1])
                        idx1 += 1
                        
                    while idx2 < len(right) and right[idx2][0] == curr:
                        right[idx2][1] += left_ptr
                        right[idx2][2] += len(left) - idx1
                        merged.append(right[idx2])
                        idx2 += 1
                elif left[idx1][0] < right[idx2][0]:
                    merged.append(left[idx1])
                    idx1 += 1
                else:
                    right[idx2][1] += idx1
                    right[idx2][2] += len(left) - idx1
                    merged.append(right[idx2])
                    idx2 += 1
                    
            while idx1 < len(left):
                merged.append(left[idx1])
                idx1 += 1
                        
            while idx2 < len(right):
                right[idx2][1] += idx1
                right[idx2][2] += len(left) - idx1
                merged.append(right[idx2])
                idx2 += 1
            return merged

        # Gives sorted array with numbers greater and less than itself only from to the left of the number it self
        sorted_arr = mergeSort(instructions)
        answer = 0
        for num in sorted_arr:
            answer += min(num[1], num[2])
        return answer % ((10 ** 9 )+ 7)
        
        
        # Better approach from discussion
        # ===============================
        
#         m = max(instructions)
#         c = [0] * (m + 1)

#         def update(x):
#             while (x <= m):
#                 c[x] += 1
#                 x += x & -x

#         def get(x):
#             res = 0
#             while (x > 0):
#                 res += c[x]
#                 x -= x & -x
#             return res

#         res = 0
#         for i, a in enumerate(instructions):
#             res += min(get(a - 1), i - get(a))
#             update(a)
#         return res % (10**9 + 7)
