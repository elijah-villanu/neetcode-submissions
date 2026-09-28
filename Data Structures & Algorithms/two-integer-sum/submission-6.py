class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_table = {}

        for i, n in enumerate(nums):
            if (target - n) in nums_table:
                return [nums_table[target-n], i]

            nums_table[n] = i
        return False
