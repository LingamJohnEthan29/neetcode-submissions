class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c:[] for c in range(numCourses)}
        for crs,pre in prerequisites:
            prereq[crs].append(pre)
        
        res = []
        visit = set()
        cycle = set()
        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            cycle.add(node)
            for pre in prereq[node]:
                if not dfs(pre):
                    return False
            cycle.remove(node)
            visit.add(node)
            res.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res

                
            
            
            
            

        