class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, n in enumerate(nums):
            comp = target - n
            if comp in nums_map:
                return [nums_map[comp], i]
            nums_map[n] = i