class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # age is set as [11:13]

        res = 0
        for p in details:
            if int(p[11:13]) > 60:
                res += 1
        return res