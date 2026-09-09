class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        # Store index of number

        for i, n in enumerate(nums):
            opp = target - n
            if opp in num_map:
                return [min(i, num_map.get(opp)), max(i, num_map.get(opp))]
            num_map[n] = i