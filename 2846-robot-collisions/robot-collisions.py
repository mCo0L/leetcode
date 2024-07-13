class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        n = len(positions)
        robots = sorted(zip(range(n), positions, healths, directions), key=lambda x: x[1])
        stack = []
        
        for i, pos, health, direction in robots:
            if direction == 'L':
                while stack and stack[-1][3] == 'R':
                    if stack[-1][2] < health:
                        health -= 1
                        stack.pop()
                    elif stack[-1][2] > health:
                        stack[-1] = (stack[-1][0], stack[-1][1], stack[-1][2] - 1, stack[-1][3])
                        break
                    else:
                        stack.pop()
                        break
                else:
                    stack.append((i, pos, health, direction))
            else:  # direction == 'R'
                stack.append((i, pos, health, direction))
        
        return [health for _, _, health, _ in sorted(stack)]