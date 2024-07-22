class Solution:
    def topological_sort(self, k: int, conditions: List[List[int]]):
        graph = defaultdict(list)
        in_degree = {i: 0 for i in range(1, k + 1)}
        
        for u, v in conditions:
            graph[u].append(v)
            in_degree[v] += 1
        
        queue = deque([node for node in in_degree if in_degree[node] == 0])
        topological_order = []
        
        while queue:
            node = queue.popleft()
            topological_order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(topological_order) == k:
            return topological_order
        else:
            return []
    
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_order = self.topological_sort(k, rowConditions)
        col_order = self.topological_sort(k, colConditions)
        
        if not row_order or not col_order:
            return []  # If either topological sort is not possible
        
        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}
        
        matrix = [[0] * k for _ in range(k)]
        
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num
        
        return matrix