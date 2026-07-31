class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        current = {}

        for i, num in enumerate(nums):
            if num in current:
                return True
            current[num] = i

            
        return False