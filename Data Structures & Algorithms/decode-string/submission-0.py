class Solution:
    def decodeString(self, s: str) -> str:
        current_num = 0
        currString = ""
        stack = []
        for i in s:
            if i.isdigit():
                current_num = current_num * 10 + int(i)
            elif i == '[':
                stack.append((currString, current_num))
                currString = ""
                current_num = 0
            elif i == ']':
                prev_string, repeat = stack.pop()
                currString = prev_string + (currString * repeat)
            else:
                currString += i
        return currString