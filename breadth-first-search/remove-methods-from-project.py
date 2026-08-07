from collections import deque
from typing import List


class Solution:

  def remainingMethods(
      self, n: int, k: int, invocations: List[List[int]]
  ) -> List[int]:
    # Step 1: Build the directed graph adjacency list
    graph = [[] for _ in range(n)]
    for u, v in invocations:
      graph[u].append(v)

    # Step 2: Find all suspicious methods reachable from method k using BFS
    suspicious = set([k])
    queue = deque([k])

    while queue:
      curr = queue.popleft()
      for neighbor in graph[curr]:
        if neighbor not in suspicious:
          suspicious.add(neighbor)
          queue.append(neighbor)

    # Step 3: Check if any non-suspicious method invokes a suspicious method
    for u, v in invocations:
      if u not in suspicious and v in suspicious:
        # Removal is invalid, return all methods
        return list(range(n))

    # Step 4: If no external incoming edge exists, return all non-suspicious methods
    return [i for i in range(n) if i not in suspicious]