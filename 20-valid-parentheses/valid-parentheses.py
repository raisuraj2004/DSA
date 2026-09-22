class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={ ')':'(','}':'{',']':'['}
        for i in s:
            if i not in pairs:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    popped=stack.pop()
                    if popped != pairs[i]:
                        return False
        return not stack

