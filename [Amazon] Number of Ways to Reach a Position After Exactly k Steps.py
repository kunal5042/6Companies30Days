# Question: https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/
# Medium

from functools import cache

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        @cache
        def memoization(position, count):
            if count > k:
                return 0
            
            if position == endPos and count == k:
                return 1
            
            return memoization(position+1, count+1) + memoization(position-1, count+1)

        return memoization(startPos, 0) % ((10 ** 9) + 7)


# January 31, 2023

'''

# Kunal Wadhwa

'''