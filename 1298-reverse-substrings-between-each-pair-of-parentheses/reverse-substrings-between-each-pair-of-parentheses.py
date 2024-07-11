class Solution:
    
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ')':
                # Pop until matching '('
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                # Pop the '('
                stack.pop()
                # Add reversed content back to stack
                stack.extend(temp)
            else:
                stack.append(ch)
        
        # Join the stack to form the final result
        return ''.join(stack)

            
        
        