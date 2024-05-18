class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '{':
                stack.append('}')
            elif item == '[':
                stack.append(']')
            elif not stack or stack.pop() != item:
                return False
        return not stack
        

s = Solution()
print(s.isValid("()"))
print(s.isValid("({})[]"))
print(s.isValid("({[]}())[{}]{[]}"))

