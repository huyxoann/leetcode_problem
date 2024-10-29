class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char not in mapping:
                stack.append(char)
            else:
                if not stack or mapping[char] != stack.pop():
                    return False
        return not stack