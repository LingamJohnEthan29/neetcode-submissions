class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in edges:
            u,v = i 
            graph[u].append(v)
            graph[v].append(u)
        num = 0
        visited = set()
        def dfs(node):
            if node in visited:
                return True
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)
        for i in range(n):
            if i not in visited:
                dfs(i)
                num += 1
        return num


        