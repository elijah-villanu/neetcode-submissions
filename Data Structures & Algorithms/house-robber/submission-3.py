class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [0] * len(nums)

        cache[0] = nums[0]
        if len(nums) >= 2: cache[1] = nums[1]
        if len(nums) >= 3: cache[2] = nums[0] + nums[2]

        for n in range(3, len(nums)):
            curr = max(cache[n - 2], cache[n - 3]) + nums[n]
            cache[n] = curr
        
        return max(cache)