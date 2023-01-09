# Question: https://leetcode.com/problems/split-array-into-consecutive-subsequences/
# Medium
from typing import Optional, List

class Solution:
    # O(n) time and O(n) space
    def isPossible(self, nums: List[int]) -> bool:
        hashmap = defaultdict(list)
        
        for num in nums:
            if num not in hashmap:
                heappush(hashmap[num+1], 1)
            else:
                length = heappop(hashmap[num])
                if len(hashmap[num]) == 0:
                    del hashmap[num]
                heappush(hashmap[num+1], length+1)
                
        for _, lengths in hashmap.items():
            for length in lengths:
                if length < 3:
                    return False
                
        return True



# January 09, 2023

'''

# Kunal Wadhwa

'''