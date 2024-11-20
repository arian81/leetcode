"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # traverse using bfs and create the copy
        if node:
            q = deque()
            q.append(node)
            visited = {}
            visited[node] = Node(node.val, [])

            while q:
                for i in range(len(q)):
                    curr_node = q.popleft()
                    for n in curr_node.neighbors:
                        if n not in visited:
                            visited[n] = Node(n.val, [])
                            q.append(n)

                        visited[curr_node].neighbors.append(visited[n])

            return visited[node]


        else:
            return node
        # newGraph = Node(node.val, )
        