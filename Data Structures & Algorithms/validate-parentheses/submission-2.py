class Solution:
    def isValid(self, s: str) -> bool:
        paren_mapping = {
        '(':')',
        '{':'}',
        '[':']'
        }
        stack = []

        for c in s:
            # Opening paranthesis
            if c in paren_mapping:
                stack.append(c)
            # Closed paranthesis
            else:
                if stack:
                    # Python lists don't have peek
                    top = stack[-1]
                    if paren_mapping[top] != c:
                        return False
                    # Valid pair
                    else:
                        stack.pop()
                else:
                    return False
        # Unclosed paranthesis
        if stack:
            return False
        return True
    