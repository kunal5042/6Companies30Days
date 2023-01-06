# Question: https://leetcode.com/problems/perfect-rectangle/
# Hard
from typing import Optional, List

class Solution:
    # O(n) time
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        corners = set()
        a = lambda: (Y-y) * (X-x)
        
        for x, y, X, Y in rectangles:
            area += a()
            corners ^= {(x,y), (x,Y), (X,y), (X,Y)}

        if len(corners) != 4: return False
        x, y = min(corners, key=lambda x: x[0] + x[1])
        X, Y = max(corners, key=lambda x: x[0] + x[1])
        
        return a() == area


# January 06, 2023

'''

# Kunal Wadhwa

'''