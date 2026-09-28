class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_table = {}

        for i, n in enumerate(nums):
            m = target - n
            if m in nums_table:
                return [nums_table[m], i]

            nums_table[n] = i
