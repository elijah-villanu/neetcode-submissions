class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
                # two pointer method
        # one pointer at t and s
        # for each character check if t is in s
        # if true iterate both, else iterate t
        if len(t) < len(s):
            return False

        i = 0
        for c in t:
            if i < len(s) and s[i] == c :
                i += 1
        
        if i >= len(s):
                return True    
        return False
