class Solution:
    def countAndRemove(self, s: str, match: str, pt: int) -> (str, int):
        char_stack = list()
        points = 0
        for ch in s:
            if ch == match[1] and char_stack and char_stack[-1] == match[0]:
                char_stack.pop()
                points += pt
            else:
                char_stack.append(ch)
        
        return "".join(char_stack), points


    
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        if x > y:
            s, pointsX = self.countAndRemove(s, 'ab', x)
            s, pointsY = self.countAndRemove(s, 'ba', y)
        else:
            s, pointsY = self.countAndRemove(s, 'ba', y)
            s, pointsX = self.countAndRemove(s, 'ab', x)
        
        return pointsX + pointsY
            
        