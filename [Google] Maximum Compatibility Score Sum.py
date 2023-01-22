# Question: https://leetcode.com/problems/maximum-compatibility-score-sum/
# Medium
from typing import Optional, List

class Solution:
    # brute-force: accepted
    # O(ROWS! * (ROWS*COLS)) time and O(ROWS) space
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        ROWS, COLS = len(students), len(students[0])
        paired = set()
        
        def get_score(srow, mrow):
            score = 0
            for col in range(COLS):
                if students[srow][col] == mentors[mrow][col]:
                    score += 1
            return score
             
        def optimal_pairs(srow):
            if srow == ROWS:
                return 0
            
            pairing = 0
            for mrow in range(len(mentors)):
                if mrow not in paired:
                    paired.add(mrow)
                    score = get_score(srow, mrow) + optimal_pairs(srow+1)
                    pairing = max(pairing, score)
                    paired.remove(mrow)
            return pairing
        
        return optimal_pairs(0)


# January 22, 2023

'''

# Kunal Wadhwa

'''