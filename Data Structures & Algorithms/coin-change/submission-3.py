import sys
sys.setrecursionlimit(20000)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # BFS are we are looking for the least amount 
        # of depth given all possible paths (shortest path)
        # Base case: when total > or = amount
        # Memoization to avoid repeated work, can be done with cache or hashmap
        # This is because the optimal coins at amount x is the same as we iterate x + 1

        cache = {}

        def bfs(i):
            # Base cases
            if i == 0:
                return 0
            # If cached, simply return
            if cache.get(i):
                return cache.get(i)

            # Try every coin and track the minimum 
            # (minimum of every path will get minimum of all paths)
            # Arbitrary large value
            minimum = 1e9
            for c in coins:
                if (i - c) >= 0:
                    minimum = min(minimum, 1 + bfs(i - c))
            
            # cache entry
            cache[i] = minimum
            return minimum
        
        min_coins = bfs(amount)
        # 1e9 flag means not possible with coins and amount
        return -1 if min_coins >= 1e9 else min_coins

