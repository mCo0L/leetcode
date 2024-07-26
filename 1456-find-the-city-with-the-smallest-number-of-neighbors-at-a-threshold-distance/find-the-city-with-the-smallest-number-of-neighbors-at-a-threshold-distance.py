class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def dijkstra(start):
            # Distance array, initialized to infinity
            distances = [float('inf')] * n
            distances[start] = 0
            # Priority queue
            pq = [(0, start)]
            while pq:
                current_distance, current_node = heapq.heappop(pq)
                # Skip if we found a better way
                if current_distance > distances[current_node]:
                    continue
                # Explore neighbors
                for neighbor, weight in graph[current_node]:
                    distance = current_distance + weight
                    # Only consider this new path if it's better
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(pq, (distance, neighbor))
            return distances
        
        min_count = n
        result_city = -1
        
        for i in range(n):
            distances = dijkstra(i)
            count = sum(1 for d in distances if d <= distanceThreshold)
            if count < min_count or (count == min_count and i > result_city):
                min_count = count
                result_city = i
        
        return result_city