class Solution:
    def isValid(self, s: str) -> bool:
        match = {'{': '}', '[': ']', '(': ')'}
        unresolved = []
        for char in s:
            if char in match.keys():
                unresolved.append(match[char])
            elif char in match.values():
                if not unresolved:
                    return False
                popped = unresolved.pop()
                if char != popped:
                    return False
        if unresolved:
            return False
        return True