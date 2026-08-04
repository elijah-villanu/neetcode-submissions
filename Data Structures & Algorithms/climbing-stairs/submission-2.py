class Solution:
    def climbStairs(self, n: int) -> int:
        # Dynamic programming approach
        # Memoization as same subproblem appears (when exploring choices)
        # As i increases, simply adding to previous sequence (like fib sequence), so only need
        # to compute from i onward
        
        # Fixed size cache
        cache = [-1] * n

        # explores/counts how many possibilites can be reached to end depth (n) recursively
        def dfs(i):
            # Base case (i lands on n, destination reached so is valid
            # and n is crossed, invalid)
            if i == n:
                return 1
            if i > n:
                return 0
            
            # Check cache, else compute via recursion
            if cache[i] != -1:
                return cache[i]
            else:
                res = dfs(i + 1) + dfs(i + 2)
                cache[i] = res
                return res
        
        return dfs(0)
        