# Question: https://leetcode.com/problems/longest-happy-prefix/
# Hard
from typing import Optional, List

class Solution:
    # O(n) time and O(1) space
    def longestPrefix(self, s):
        mod = 10 ** 9 + 7
        result = 0
        # hash key for prefix and suffix
        left, right = 0, 0
        
        for idx in range(len(s) - 1):
            left = (left * 128 + ord(s[idx])) % mod
            right = (right + pow(128, idx, mod) * ord(s[~idx])) % mod
            
            # checking if the prefix and suffix agrees
            if left == right:
                result = idx + 1

        return s[:result]


# January 06, 2023

'''

# Kunal Wadhwa

'''