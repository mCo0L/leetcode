class Solution:
    def countOfAtoms(Self, formula: str) -> str:
        stack = [collections.defaultdict(int)]
        i, n = 0, len(formula)
        
        while i < n:
            if formula[i] == '(':
                stack.append(collections.defaultdict(int))
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[i_start:i] or 1)
                for name, count in top.items():
                    stack[-1][name] += count * multiplier
            else:
                i_start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                name = formula[i_start:i]
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[i_start:i] or 1)
                stack[-1][name] += count
        
        result = []
        for name in sorted(stack[-1].keys()):
            count = stack[-1][name]
            result.append(name)
            if count > 1:
                result.append(str(count))
        
        return ''.join(result)