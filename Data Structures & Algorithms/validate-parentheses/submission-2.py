class Solution:
    def isValid(self, s: str) -> bool:
        p_dict = {')': '(', '}': '{', ']': '['}
        stack = deque()
        # print(p_dict.values())
        for c in s:
            if c in p_dict.values():
                stack.append(c)
            else:
                if stack and p_dict[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return False if stack else True


        