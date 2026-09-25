class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Brute Force: continously check every element to right to see the largest and track

        # Optimize: Instead, store the largest and it's index after first pass
        # Once index passed, get the next largest (look right only) and index and repeat
        # Worst case: each one increases which prompts an array check each time

        largest = -1
        largest_index = 0
        res = []

        for i, n in enumerate(arr):
            if i == (len(arr) - 1):
                res.append(-1)
                continue
            # Find largest
            if i == largest_index:
                largest = max(arr[i+1:])
                largest_index = i + 1 + arr[i+1:].index(largest)
            
            res.append(largest)
                    
        return res