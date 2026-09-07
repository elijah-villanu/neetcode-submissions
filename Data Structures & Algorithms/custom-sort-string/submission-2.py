class Solution:
    def customSortString(self, order: str, s: str) -> str:
        key = {}

        # Build key, ranked by appearance
        for i, ch in enumerate(order):
            key[ch] = i

        return "".join(sorted(s, key=lambda ch: key.get(ch, 26))) 