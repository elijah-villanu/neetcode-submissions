class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O(n) solution is counting each with a hashmap and returning the max value
        nums_table = Counter(nums)
        return max(nums_table, key=nums_table.get)