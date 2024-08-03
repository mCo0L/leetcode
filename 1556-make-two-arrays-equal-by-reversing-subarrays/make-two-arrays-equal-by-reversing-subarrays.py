class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counter = {}
        for a in arr:
            counter[a] = counter.get(a, 0) + 1
        
        for b in target:
            val = counter.get(b)
            if not val or val == 0:
                return False
            
            counter[b] = val-1
        
        for _, val in counter.items():
            if val != 0:
                return False
        
        return True