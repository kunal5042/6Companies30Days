# Question: https://leetcode.com/problems/destroying-asteroids/
# Medium

from typing import Optional, List

class Solution:
    # O(n * log(n)) time and O(1) space
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        
        for ast_mass in asteroids:
            if mass < ast_mass: return False
            mass += ast_mass
        
        return True


# January 30, 2023

'''

# Kunal Wadhwa

'''