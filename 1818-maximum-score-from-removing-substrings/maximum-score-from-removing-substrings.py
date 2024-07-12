class Solution:
    def countAndRemove(self, s: str, match: str, pt: int) -> (str, int):
        l = len(s)
        i = 0
        points = 0
        while(i < l):
            if s[i:i+2] == match:
                points += pt
                s = s[:i] + s[i+2:]

                # since it's possible that because we are remove a part of string the previous char might form a new match
                i -= 1
            else:
                i += 1
        
        return s, points

    
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        if x > y:
            s, pointsX = self.countAndRemove(s, 'ab', x)
            s, pointsY = self.countAndRemove(s, 'ba', y)
        else:
            s, pointsY = self.countAndRemove(s, 'ba', y)
            s, pointsX = self.countAndRemove(s, 'ab', x)
        
        return pointsX + pointsY
            
        