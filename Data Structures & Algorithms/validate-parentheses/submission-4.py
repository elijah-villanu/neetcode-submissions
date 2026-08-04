class Solution:
    def isValid(self, s: str) -> bool:
        paran_mapping = {
            '(':')',
            '{':'}',
            '[':']'
        }
        # Stack ensures open brackets are closed in the correct order
        stack = []

        # Two cases: open or closed
        for c in s:
            # Open
            if c in paran_mapping:
                stack.append(c)
                continue
            
            # Closed
            # Check if closed corresponds to the correct open
            if stack:
                if paran_mapping.get(stack[-1]) == c:
                    stack.pop()
                else:
                    return False
            else:
                return False

        if stack:
            return False
        return True
            
            
            