# Question: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
# Medium
from typing import Optional, List
from heapq import heapify, heappop, heappush

class Node:
    def __init__(self, _id):
        self.id = _id
        self.adjacents = set()
        
    def connect_with(self, node2, weight) -> None:
        """Connects node2 with self"""
        self.adjacents.add((weight, node2))
        
    def __lt__(self, other_node):
        """Compares other_node object with self for priority calculation"""
        return self.id < other_node.id
        
class Graph:
    def __init__(self, n, adj_list):
        self.nodes = {}
        self.initialize_nodes(n)
        self.build_graph(adj_list)
        
    def initialize_nodes(self, node_count: int) -> None:
        """Creates node_count node objects"""
        for node_id in range(node_count):
            self.nodes[node_id] = Node(node_id)
    
    def build_graph(self, adj_list) -> None:
        """Adds edges among nodes"""
        for (source, dest, time) in adj_list:
            self.nodes[source].connect_with(self.nodes[dest], time)
            self.nodes[dest].connect_with(self.nodes[source], time)
            
    def get_ways_to_reach_destination_in_shortest_time(self, source, dest):
        dest_node = self.nodes[dest]
        unexplored = [(0, self.nodes[source])]
        heapify(unexplored)
        explored = set()
        times = [float('inf') for _ in range(len(self.nodes))]
        times[source] = 0
        ways = [0 for _ in range(len(self.nodes))]
        ways[source] = 1
        mod = (10**9) + 7        
        
        while len(unexplored) != 0:
            time, node = heappop(unexplored)
            
            if node in explored: continue
            explored.add(node)
            
            for adj_time, adj_node in node.adjacents:
                if adj_node in explored: continue
                
                new_discovered_time = time + adj_time
                
                if new_discovered_time == times[adj_node.id]:
                    ways[adj_node.id] += ways[node.id]
                    
                elif new_discovered_time < times[adj_node.id]:
                    ways[adj_node.id] = ways[node.id]
                    times[adj_node.id] = new_discovered_time
                    heappush(unexplored, (new_discovered_time, adj_node))
                    
        return ways[~0] % mod
        
class Solution:
    # O(M * logN + N) time and O(M + N) space
    # where M <= N*(N-1)/2 is number of roads, N <= 200 is number of intersections.
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = Graph(n, roads)
        return graph.get_ways_to_reach_destination_in_shortest_time(0, n-1)


# January 01, 2023

'''

# Kunal Wadhwa

'''