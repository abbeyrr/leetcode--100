class Solution:
    def trap(self, height):
        ans = 0
        left, right = 0, len(height) - 1
        leftmax = rightmax = 0

        while left < right:
            leftmax = max(leftmax, height[left])
            rightmax = max(rightmax, height[right])
            if height[left] < height[right]:
                ans += leftmax - height[left]
                left += 1

            else:
                ans += rightmax - height[right]
                right -= 1

        return ans
    
# time complexity: O(n)