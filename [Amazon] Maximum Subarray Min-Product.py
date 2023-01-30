# Question: https://leetcode.com/problems/maximum-subarray-min-product/
# Medium

from typing import Optional, List
class Solution:
    # O(n) time and O(n) space
    def maxSumMinProduct(self, nums: List[int]) -> int:
        prev_smaller, next_smaller = [None]*len(nums), [None]*len(nums)

        # build the next smaller array
        stack = []
        for idx in reversed(range(len(nums))):
            while len(stack) != 0 and nums[stack[~0]] >= nums[idx]: stack.pop()
            next_smaller[idx] = -1 if len(stack) == 0 else stack[~0]
            stack.append(idx)

        # build the previous smaller array
        stack.clear()
        for idx in range(len(nums)):
            while len(stack) != 0 and nums[stack[~0]] >= nums[idx]: stack.pop()
            prev_smaller[idx] = -1 if len(stack) == 0 else stack[~0]
            stack.append(idx)

        # stores the maximum subarray min-product
        result = float('-inf')
        
        # build the prefix sum for optimisation
        prefix_sum = [0 for _ in range(len(nums)+1)]
        for idx in range(len(nums)):
            prefix_sum[idx + 1] = prefix_sum[idx] + nums[idx]
                
        # find the maximum min-product for every element and keep track of the largest value
        for idx in range(len(nums)):
            # subarray end
            end   = len(nums)-1 if next_smaller[idx] == -1 else next_smaller[idx] - 1
            # subarray start
            start = 0 if prev_smaller[idx] == -1 else prev_smaller[idx] + 1
            
            subarray_sum = prefix_sum[end+1] - prefix_sum[start]
            
            # current element is the minimum in this subarray
            result = max(result, subarray_sum * nums[idx])

        return result % ((10**9)+7)

# January 29, 2023

'''

# Kunal Wadhwa

'''