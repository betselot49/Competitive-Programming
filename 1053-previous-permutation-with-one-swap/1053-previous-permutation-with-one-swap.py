class Solution:
    def prevPermOpt1(self, A):
        i = len(A) - 2
        while i >= 0 and A[i] <= A[i+1]:
            i -= 1
        if i >= 0:
            max_ = i + 1
            for j in range(max_ + 1, len(A)):
                if A[max_] < A[j] < A[i]: 
                    max_ = j
            A[max_], A[i] = A[i], A[max_]
        return A