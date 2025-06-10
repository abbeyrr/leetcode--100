class Solution():
    def moveZero(self, nums):
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left] , nums[right] = nums[right], nums[left]   
                left += 1
            right += 1

# time complexity: O(n)    