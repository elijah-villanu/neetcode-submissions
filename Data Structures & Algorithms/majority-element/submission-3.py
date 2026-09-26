class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O(1) space and linear time
        nums.sort()

        # appears more than n/2 times, so will be the right element from the center
        mid = len(nums) // 2
        return nums[mid]