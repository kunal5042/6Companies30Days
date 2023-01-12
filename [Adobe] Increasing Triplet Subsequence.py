# Question: https://leetcode.com/problems/increasing-triplet-subsequence/
# Medium
from typing import Optional, List

class Solution:
    # brute-force   
    # O(n*n) time and O(1) space
    def increasingTriplet(self, nums: List[int]) -> bool:
        for jdx in range(1, len(nums)-1):
            idx = jdx - 1
            kdx = jdx + 1
            while idx >= 0 and nums[idx] >= nums[jdx]:
                idx -= 1
            while kdx < len(nums) and nums[jdx] >= nums[kdx]:
                kdx += 1
            
            if idx >= 0 and kdx < len(nums):
                return True
        return False
    
    # optimized
    # O(n) time and O(1) space
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        first = second = float('inf')
        
        for ele in nums:
            if ele <= first:
                first = ele
                
            elif ele <= second:
                second = ele
                
            else:
                return True
        
        return False


# January 12, 2023

'''

# Kunal Wadhwa

'''