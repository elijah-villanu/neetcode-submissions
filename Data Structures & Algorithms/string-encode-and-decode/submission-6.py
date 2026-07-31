class Solution:

    def encode(self, strs: List[str]) -> str:
        # Encoding approach: start with a number for length of string, with # marking the end of size section
        if not strs:
            return ""
        
        sizes, res = [], []
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res.append(str(sz))
            res.append(',')
        res.append('#')
        res.extend(strs)

        # Combines all strings into one string
        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        # Decoding approach: read number of characters until reaching #
        if not s:
            return []
        sizes = []
        decoded = []
        i = 0

        # Read in sizes first
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            # Sizes are delimited by ',' so index start to end
            sizes.append(int(s[i:j]))
            i = j + 1
        # End of '#'
        i += 1

        # Read up to each size string and append
        for sz in sizes:
            decoded.append(s[i:i + sz])
            i += sz
        return decoded