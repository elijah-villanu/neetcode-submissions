class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dfs(i):
            if i >= n:
                return i == n
            elif i in cache:
                return cache[i]
            else:
                cache[i] = dfs(i+1) + dfs(i+2)
                return cache[i]
        
        return dfs(0)