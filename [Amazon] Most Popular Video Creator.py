# Question: https://leetcode.com/problems/most-popular-video-creator/
# Medium

from typing import Optional, List
from collections import defaultdict
from heapq import heapify, heappop, heappush

class Solution:
    # O(n) time and O(n) space
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        def get_best_content_id(creator):
            content = creator_info[creator]
            heapify(content)
            return [content[0][1]]
        
        creator_info = defaultdict(list)
        creator_popul = defaultdict(int)
        
        for idx in range(len(creators)):
            creator_info[creators[idx]].append((-views[idx], ids[idx]))
            creator_popul[creators[idx]] += views[idx]
            
        max_popul = None
        best_creators = []
        for creator, popularity in creator_popul.items():
            if max_popul is None:
                max_popul = popularity
                best_creators.append(creator)
                continue
            
            if popularity == max_popul:
                best_creators.append(creator)
                
            elif popularity > max_popul:
                max_popul = popularity
                best_creators = [creator]
                
        result = []
        for creator in best_creators:
            stats = [creator]
            for content_id in get_best_content_id(creator):
                stats.append(content_id)
            result.append(stats)
            
        return result
            

# January 30, 2023

'''

# Kunal Wadhwa

'''