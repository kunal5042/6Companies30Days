# Question: https://leetcode.com/problems/new-21-game/
# Medium
from typing import Optional, List

class Solution:
    # O(n) time and O(n) space
    def new21Game(self, n: int, k: int, max_points: int) -> float:
        if k == 0 or n >= k + max_points: return 1
        
        dp = [1.0] + [0.0] * n
        mpsum = 1.0
        
        for idx in range(1, n + 1):
            dp[idx] = mpsum / max_points
            if idx < k:
                mpsum += dp[idx]
                
            if idx - max_points >= 0:
                mpsum -= dp[idx - max_points]
                
        return sum(dp[k:])


# January 21, 2023

'''

# Kunal Wadhwa

'''