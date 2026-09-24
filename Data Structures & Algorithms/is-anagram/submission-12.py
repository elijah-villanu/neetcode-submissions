class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # regardless of order, as long as each letter appearance matches
        s_dict = {}
        t_dict = {}

        # key is letter: value is num appearances, can do simple dictionary compare

        # build s and t dict while iterating as both should be of same length
        for i, s_char in enumerate(s):
            t_char = t[i]
            s_dict[s_char] = s_dict.get(s_char, 0) + 1
            t_dict[t_char] = t_dict.get(t_char, 0) + 1
        
        if s_dict == t_dict:
            return True
        return False