class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for j, n in enumerate(nums):
            comp = target - n
            if comp in seen:
                return [seen[comp], j]
            seen[n] = j
        
        return False