# Question: from collections import Counter
#     # O(N * Log(K)) Time And O(N) Space
from typing import Optional, List

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        return [word for word, freq in Counter(words).most_common(k)]


# January 19, 2023

'''

# Kunal Wadhwa

'''