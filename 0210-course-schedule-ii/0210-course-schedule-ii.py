class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [False for _ in range(numCourses)]
        finished = []
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        def dfs(prereq):
            for course in graph[prereq]:
                if not visited[course]:
                    visited[course] = True
                    if not dfs(course): return False  # unable to finish course
                elif course not in finished:          # cycle in graph
                    return False
            finished.append(prereq)
            return True
        for i in range(numCourses):   # visit all trees in graph
            if not visited[i]:
                visited[i] = True
                if not dfs(i): return []
        finished.reverse()    # topological ordering = reverse finish time
        return finished 