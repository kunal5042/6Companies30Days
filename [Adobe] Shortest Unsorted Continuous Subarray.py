# Question: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# Medium
from typing import Optional, List
from collections import defaultdict
class Solution:
    # O(n * log(n)) time and O(n) space
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_index = defaultdict(set)
        for idx, ele in enumerate(sorted(nums)):
            sorted_index[ele].add(idx)
            
        start = end = None
        for idx in range(len(nums)):
            if idx not in sorted_index[nums[idx]]:
                if start is None:
                    start = idx
                    continue
                end = idx

        if start is None: return 0
        return end - start + 1
    
    # O(n) time and O(n) space using Monotonic stack
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        start, end = float('inf'), float('-inf')
        for idx in range(len(nums)):
            while len(stack) != 0 and nums[stack[~0]] > nums[idx]:
                start = min(start, stack.pop())
            stack.append(idx)
                
        del stack
        stack = []
        for idx in range(len(nums)-1, -1, -1):
            while len(stack) != 0 and nums[stack[~0]] < nums[idx]:
                end = max(end, stack.pop())
            stack.append(idx)
        
        length = end - start + 1
        return length if length > 0 else 0


# January 01, 2023

'''

# Kunal Wadhwa

'''