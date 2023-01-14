# Question: https://leetcode.com/problems/dungeon-game/
# Hard
from typing import Optional, List

class Solution:
    # O(m * n) time and O(m * n) space
    def calculateMinimumHP(self, dungeon):
        ROWS, COLS = len(dungeon), len(dungeon[0])
        min_hp = [[float('inf') for _ in range(COLS+1)] for _ in range(ROWS+1)]
        min_hp[ROWS-1][COLS] = 1
        min_hp[ROWS][COLS-1] = 1
        
        for row in range(ROWS-1, -1, -1):
            for col in range(COLS-1, -1, -1):
                min_hp[row][col] = max(
                    min(
                        min_hp[row+1][col],
                        min_hp[row][col+1],
                    ) - dungeon[row][col],
                    1
                )
        return min_hp[0][0]


# January 14, 2023

'''

# Kunal Wadhwa

'''