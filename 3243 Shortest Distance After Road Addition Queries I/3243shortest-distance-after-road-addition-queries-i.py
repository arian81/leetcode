class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        res = []
        # make graph
        for i in range(n - 1):
            adj[i].append(i + 1)

        def bfs(node):
            seen = set()
            q = deque()
            q.append(node)
            seen.add(node)
            length = 1
            while q:
                for i in range(len(q)):
                    curr_node = q.popleft()
                    
                    for j in adj[curr_node]:
                        if j in seen :
                            continue
                        
                        if j == n - 1:
                            return length
                        q.append(j)
                        seen.add(j)
                length += 1
        
        for src, dest in queries:
            adj[src].append(dest)
            res.append(bfs(0))
        
        return res

        print(adj)


        