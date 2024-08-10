class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        #build the graph
        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
            graph[pre[0]] += 1
        
        queue = Deque()
        #find zero nodes
        for idx in range(numCourses):
            if graph[idx] == 0:
                queue.append(idx)
        
        visited = 0
        while queue:
            node = queue.popleft()
            visited += 1
            for neighbour in adj[node]:
                #remove the course
                graph[neighbour] -= 1
                if graph[neighbour] == 0:
                    queue.append(neighbour)
        #if we visit the course twice means cycle is there
        return visited == numCourses