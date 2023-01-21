# Question: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
# Medium
from typing import Optional, List

from heapq import heapify, heappop, heappush
class Node:
    def __init__(self, label):
        self.label = label
        self.connected = set()
        
    def __lt__(self, other_node_object):
        return self.label < other_node_object.label
        
class Graph:
    def __init__(self):
        self.nodes = {}
        self.threshold = None
        
    def initialize_nodes(self, node_count):
        for node_no in range(node_count):
            self.nodes[node_no] = Node(node_no)
        
    def build_graph(self, edges):
        for _from, _to, _weight in edges:
            self.nodes[_from].connected.add((self.nodes[_to], _weight))
            self.nodes[_to].connected.add((self.nodes[_from], _weight))
            
    def dijkstra(self, source) -> List[int]:
        distances = [float('inf') for _ in range(len(self.nodes))]
        distances[source] = 0
        explored  = set()
        unexplored = [(0, self.nodes[source])]
        
        while len(unexplored) != 0:
            weight, vertex = heappop(unexplored)
            
            if vertex in explored: continue
            explored.add(vertex)
            
            for adjacent, adj_weight in vertex.connected:
                if adjacent in explored: continue
                if weight + adj_weight > self.threshold: continue
                                    
                cost_to_adj = weight + adj_weight
                if cost_to_adj < distances[adjacent.label]:
                    distances[adjacent.label] = cost_to_adj
                    heappush(unexplored, (weight+adj_weight, adjacent))
                    
        return distances
            
            
    def find_the_city(self, threshold):
        self.threshold = threshold
        result_city, result_city_neighbors = None, float('inf')
        for source in range(len(self.nodes)):
            neighbors_under_threshold = 0

            for city, distance_to_city_from_source in enumerate(self.dijkstra(source)):
                if distance_to_city_from_source <= threshold:
                    neighbors_under_threshold += 1
                
            if neighbors_under_threshold == result_city_neighbors:
                if source > result_city: result_city = source
        
            if neighbors_under_threshold < result_city_neighbors:
                result_city = source
                result_city_neighbors = neighbors_under_threshold
                
        return result_city
        
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = Graph()
        graph.initialize_nodes(n)
        graph.build_graph(edges)
        return graph.find_the_city(distanceThreshold)


# January 21, 2023

'''

# Kunal Wadhwa

'''