class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # key is number, value is frequency
        appearance_count = {}
        for num in nums:
            # Count the frequency of each number
            appearance_count[num] = 1 + appearance_count.get(num, 0)
        
        # Create the array of lists and sort the array by frequency
        arr = []
        for num, cnt in appearance_count.items():
            arr.append([cnt, num])
        arr.sort()

        # return k elements at the top(pop) of list and only return num not frequency
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
