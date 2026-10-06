class Solution:
    def search(self, nums: List[int], target: int, lo=0, hi=None) -> int:
        if hi is None:
            hi = len(nums) - 1
        if lo > hi:
            return -1

        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.search(nums, target, mid + 1, hi)
        else:
            return self.search(nums, target, lo, mid - 1)