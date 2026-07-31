class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        s_dict = {}
        t_dict = {}
        for i, letter in enumerate(s):
            t_letter = t[i]
            s_dict[letter] = s_dict.get(letter, 0) + 1
            t_dict[t_letter] = t_dict.get(t_letter, 0) + 1
        
        if s_dict != t_dict:
            return False
        
        return True