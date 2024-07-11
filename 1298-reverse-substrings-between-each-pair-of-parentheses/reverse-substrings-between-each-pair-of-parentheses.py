class Solution:
    
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = [0] * n
        open_parentheses_indices = []

        for i, ch in enumerate(s):
            if ch == '(':
                open_parentheses_indices.append(i)
            elif ch == ')':
                j = open_parentheses_indices.pop()
                pair[i] = j
                pair[j] = i
        
        result = list()
        cur_index = 0
        direction = 1

        while(cur_index < n):
            if s[cur_index] in ('(', ')'):
                cur_index = pair[cur_index]
                direction = -direction
            else:
                result.append(s[cur_index])
            cur_index += direction

        return "".join(result)

            
        
        