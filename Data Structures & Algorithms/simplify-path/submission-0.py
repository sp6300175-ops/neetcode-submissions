class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = path.split("/")
        stack = []
        final = ''
        for i in lst:
            if i == "" or i == ".":
                continue
            elif i == "..":
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(i)

        if len(stack) == 0:
            return '/'
        else:
            for i in stack:
                final += '/' + i

        return final
