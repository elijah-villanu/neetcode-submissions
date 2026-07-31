class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            current_res = target - num
            if current_res in num_map:
                return [min(num_map[current_res], i), max(num_map[current_res], i)]
            num_map[num] = i
