# Question: https://leetcode.com/problems/top-k-frequent-words/
# Medium
from typing import Optional, List

from collections import Counter
class Solution:
    # O(n * log(k)) time and O(n) space
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        return [word for word, freq in Counter(words).most_common(k)]


# January 19, 2023

'''

# Kunal Wadhwa

'''