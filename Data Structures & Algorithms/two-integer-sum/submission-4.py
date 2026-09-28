class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_table = {}

        for i, n in enumerate(nums):
            m = target - n
            if m in nums_table:
                return [min(i, nums_table[m]), max(i, nums_table[m])]

            nums_table[n] = i
