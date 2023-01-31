# Question: https://leetcode.com/problems/top-k-frequent-words/
# Medium

from collections import Counter
from heapq import heapify, heappop
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = [(-freq, word) for word, freq in Counter(words).items()]
        heapify(heap)
        result = []
        
        while len(heap) != 0 and k > 0:
            result.append(heappop(heap)[1])
            k -= 1
        
        return result


# January 31, 2023

'''

# Kunal Wadhwa

'''