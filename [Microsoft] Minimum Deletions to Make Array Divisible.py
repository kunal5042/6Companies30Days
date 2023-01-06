# Question: https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/
# Hard
from typing import Optional, List

class Solution:
    # O(n) time and O(1) space
    def minOperations(self, A: List[int], numsDivide: List[int]) -> int:
        A.sort()
        g = gcd(*numsDivide)
        for i,a in enumerate(A):
            if g % a == 0: return i
            if a > g: break
        return -1


# January 06, 2023

'''

# Kunal Wadhwa

'''