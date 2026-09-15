class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        length = len(s)
        mapping = { ']' : '[', ')' : '(', '}' : '{'}
        if length == 0 or length%2!=0:
            return False
        if s[0] == ']' or s[0] == '}' or s[0] == ')':
            return False
        for c in s:
            if c == '{' or c == '[' or c == '(':
                stack.append(c)
        # for c in s:
            if len(stack) == 0 and c in [']', ')', '}']:
                return False
            # if c in [']', ')', '}'] and stack[-1] in ['[', '(', '{']:
            #     return False
            if len(stack) != 0 and c in [']', ')', '}']:
                if stack[-1] == mapping[c]: stack.pop()
                else: return False
            # else: return False
        if stack:
            return False
        else:
            return True
        