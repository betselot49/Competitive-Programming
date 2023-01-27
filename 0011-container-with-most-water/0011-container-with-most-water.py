class Solution:
    def maxArea(self, height: List[int]) -> int:
        #https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg
        maxArea = 0
        left = 0
        right = len(height) - 1
        while left <= right:
            leftHeight = height[left]
            rightHeight = height[right]
            maxArea = max(maxArea, min(leftHeight, rightHeight) * (right - left))
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return maxArea
            