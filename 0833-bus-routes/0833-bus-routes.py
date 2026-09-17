class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        bus_stops = {}
        #route map
        for idx, route in enumerate(routes):
            for stop in route:
                if stop not in bus_stops:
                    bus_stops[stop] = []
                bus_stops[stop].append(idx)
        #edge case
        if source not in bus_stops:
            return -1

        # print(bus_stops)
        visited = set()
        queue = deque()
        for bus in bus_stops.get(source, []):
            queue.append((bus, 1))
            visited.add(bus)
        
        while queue:
            current, buses_taken  = queue.popleft()

            for stop in routes[current]:
                if stop == target:
                    return buses_taken 
                
                # loop for bfs
                for connected_bus in bus_stops[stop]:
                    if connected_bus not in visited:
                        queue.append((connected_bus, buses_taken  + 1))
                        visited.add(connected_bus)            

        return -1