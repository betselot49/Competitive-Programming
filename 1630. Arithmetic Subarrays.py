class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = []
        for i in range(len(l)):
            temp, ans = nums[l[i]:r[i] + 1], True
            temp.sort()
            if len(temp) == 1:
                ans = False
                output.append(ans)
            else:
                diff, j = temp[0] - temp[1], 1
                while j < len(temp):
                    if diff != temp[j - 1] - temp[j]:
                        ans = False
                        break
                    j += 1
                output.append(ans)
        return output
