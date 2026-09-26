class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Palindromes: are mirrors from the center
        # strip and convert to lowercase and two poiner to center
        # if odd length, can't be 

        c = "".join(filter(str.isalnum, s)).lower()
        
        i = 0
        j = len(c) - 1

        while i < j:
            if c[i] != c[j]:
                return False
            i += 1
            j -= 1
        
        return True
        
