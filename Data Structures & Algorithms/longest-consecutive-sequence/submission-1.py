class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # for lookups if num-1 exists and lookups without sorting
        nums_set = set(nums)

        # A sequence starter is only defined if n-1 does not exist
        longest = 0
        for n in nums_set:
            prev = n - 1
            if prev not in nums_set:
                # ensures all sequences are accounted for
                # start new sequence once start is found
                length = 1
                while (n + length) in nums_set:
                    length += 1
                
                # log this sequence
                longest = max(length, longest)
        
        return longest


            



        
        