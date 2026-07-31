class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for i, current_str in enumerate(strs):
            # Count frequency of each letter in word (anagrams share count)
            count = [0] * 26
            for letter in current_str:
                # Maps alphabebetic letter to array index (a is index 0, etc.)
                count[ord(letter) - ord('a')] += 1
            
            # Only tuples can be keys
            mapping[tuple(count)].append(current_str)
        
        return list(mapping.values())
