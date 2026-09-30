class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Count of letters are equal to be an anagram (order doesn't matter)
        # iterate through and see if letter count in set
        # letters will be tracked by array count of 26 (lower case constraint)

        s_map = {}
        res = []

        for s in strs:
            # make array representation
            s_arr = [0] * 27
            for l in s:
                s_arr[ord(l) - 97] += 1
            s_arr = tuple(s_arr)

            # has anagram, add to existing list of anagrams from index
            if s_arr in s_map:
                res[s_map[s_arr]].append(s)
            else:
                s_map[s_arr] = len(res)
                res.append([s])
        return res