'''Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the
relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
a. 1 <= nums.length <= 10^4
b. -2^31 <= nums[i] <= 2^31 - 1'''

class Solution:
    def moveZeroes(self, nums: list) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0 and nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]

            if nums[i] != 0:
                i += 1


nums = [0, 1, 0, 3, 12]
ans=Solution()
ans.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

