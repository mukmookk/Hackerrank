#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
from collections import defaultdict, deque
import heapq

# BFS 버전
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    graph = defaultdict(list)
    for node1, node2 in zip(graph_from, graph_to):
        graph[node1].append(node2)
        graph[node2].append(node1)

    # Find nodes with the desired color
    target_nodes = [i for i in range(1, graph_nodes + 1) if ids[i-1] == val]

    min_dist = float('inf')
    for target_node in target_nodes:
        visited = [False] * (graph_nodes + 1)
        distances = [-1] * (graph_nodes + 1)
        queue = deque([(target_node, 0)])
        visited[target_node] = True

        while queue:
            node, dist = queue.popleft()
            distances[node] = dist

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, dist + 1))
                    if ids[neighbor - 1] == val:
                        min_dist = min(min_dist, dist + 1)

    return -1 if min_dist == float('inf') else min_dist

# 다익스트라 버전
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    
    # build graph
    graph = defaultdict(list)
    for node1, node2 in zip(graph_from, graph_to):
        graph[node1].append(node2)
        graph[node2].append(node1)
        
    # Insert color info
    colors = [-1] * (len(ids) + 1)
    for i in range(1, len(ids) + 1):
        colors[i] = ids[i-1]
        
    min_dist = float('inf')
    # append every id = val
    for start_node in range(1, graph_nodes + 1):
        if colors[start_node] != val:
            continue
        visited = [float('inf')] * (graph_nodes + 1)
        visited[start_node] = 0
        pq = [(0, start_node)]
        
        while pq:
            dist, node = heapq.heappop(pq)

            if dist > visited[node]:
                continue
            
            for n_node in graph[node]:
                if visited[n_node] > dist + 1:
                    visited[n_node] = dist + 1
                    heapq.heappush(pq, (visited[n_node], n_node))
            
        for node in range(1,   graph_nodes + 1):
            if node != start_node and colors[node] == val:
                min_dist = min(min_dist, visited[node])
    
    return min_dist if min_dist != float('inf') else -1

if __name__ == '__main__':

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)
    print(ans)

