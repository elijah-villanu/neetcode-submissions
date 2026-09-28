class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # We know something can only be a sequence if
        # its previous iteration exists (i - 1), else start of new sequence
        # We can use a hash set of visited 

        nums_set = set(nums)

        longest = 0
        for n in nums:
            # new sequence
            if (n - 1) not in nums_set:
                # count how long this sequence is
                curr = n
                while curr in nums_set:
                    curr += 1
                longest = max(longest, curr - n)
        
        return longest
                    