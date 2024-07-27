class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Number of lowercase English letters
        n = 26
        
        # Initialize the cost matrix with infinity
        inf = float('inf')
        cost_matrix = [[inf] * n for _ in range(n)]
        
        # Set cost 0 for converting a character to itself
        for i in range(n):
            cost_matrix[i][i] = 0
        
        # Map characters to indices 0 to 25
        char_to_index = lambda c: ord(c) - ord('a')
        
        # Populate the initial costs based on the input
        for o, c, z in zip(original, changed, cost):
            cost_matrix[char_to_index(o)][char_to_index(c)] = min(cost_matrix[char_to_index(o)][char_to_index(c)], z)
        
        # Floyd-Warshall algorithm to find all pairs shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if cost_matrix[i][j] > cost_matrix[i][k] + cost_matrix[k][j]:
                        cost_matrix[i][j] = cost_matrix[i][k] + cost_matrix[k][j]
        
        # Calculate the total minimum cost to convert source to target
        total_cost = 0
        for s, t in zip(source, target):
            s_idx = char_to_index(s)
            t_idx = char_to_index(t)
            if cost_matrix[s_idx][t_idx] == inf:
                return -1
            total_cost += cost_matrix[s_idx][t_idx]
        
        return total_cost

