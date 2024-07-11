class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True
        return False

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        result = []
        
        for u, v in requests:
            root_u = uf.find(u)
            root_v = uf.find(v)
            can_be_friends = True
            
            if root_u != root_v:
                for x, y in restrictions:
                    root_x = uf.find(x)
                    root_y = uf.find(y)
                    if (root_u == root_x and root_v == root_y) or (root_u == root_y and root_v == root_x):
                        can_be_friends = False
                        break
            
            if can_be_friends:
                uf.union(u, v)
                result.append(True)
            else:
                result.append(False)
        
        return result