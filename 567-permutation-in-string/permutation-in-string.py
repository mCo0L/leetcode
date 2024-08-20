class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, w = Counter(s1), len(s1)
        window_cntr = Counter(s2[:w])
        
        if cntr == window_cntr:
            return True
            
        for i in range(w, len(s2)):
            window_cntr[s2[i-w]] -= 1
            window_cntr[s2[i]] = window_cntr.get(s2[i], 0) + 1
            
            if all([cntr[key] == window_cntr.get(key, 0) for key in cntr.keys()]): 
                return True
        return False
    