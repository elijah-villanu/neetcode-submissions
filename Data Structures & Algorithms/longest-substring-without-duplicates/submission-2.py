class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window approach, everything is unique inside window
        # Hashset tracks if unique in O(1)
        char_set = set()
        l = 0
        count = 0
        
        for r in range(len(s)):
            while s[r] in char_set:
                # no longer duplicate, window moves
                char_set.remove(s[l])
                l += 1
            # is unique character
            char_set.add(s[r])
            # max of current window or previous window
            count = max(count, r - l + 1)
        
        return count
                


            