# Question: https://leetcode.com/problems/maximum-good-people-based-on-statements/
# Hard

from typing import Optional, List
class Solution:
    # O(n^2 * 2^n) time and O(n) space
    def maximumGood(self, statements: List[List[int]]) -> int:
        # the idea is to explore all possibilites
        # to check both conditions of a person being good or bad
        # for every person
        # and verifying if that assumption is valid or not

        def is_valid(current):
            for idx in range(len(statements)):
                if current[idx] == 1:
                    for jdx in range(len(statements)):
                        if statements[idx][jdx] != 2 and statements[idx][jdx] != current[jdx]:
                            return False
            return True
        
        result = 0
        def depth_first_search(current, idx, count):
            nonlocal result
            if idx == len(statements):
                if is_valid(current):
                    result = max(result, count)
                return
            current.append(0)
            depth_first_search(current, idx+1, count)
            current[~0] = 1
            depth_first_search(current, idx+1, count+1)
            current.pop()
            
        depth_first_search([], 0, 0)
        return result

# January 10, 2023

'''

# Kunal Wadhwa

'''