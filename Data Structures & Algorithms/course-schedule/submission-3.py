class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hash_map = defaultdict(list)
        for course in prerequisites:
            take, req = course
            if take == req:
                return False
            hash_map[take].append(req)
        def hasCycle(graph):
            visited = set()
            path = set()
            def dfs(node):
                if node in path:
                    return True
                if node in visited:
                    return False
                visited.add(node)
                path.add(node)

                for neighbour in graph[node]:
                    if dfs(neighbour):
                        return True
                path.remove(node)
                return False
            for node in range(numCourses):
                if node not in visited:
                    if dfs(node):
                        return True
            return False
        if hasCycle(hash_map):
            return False
        return True


        