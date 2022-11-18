class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')':'(',']':'[','}':'{'}

        for c in s:
            if c not in hashmap:
                stack.append(c)
            else:
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    print(False)
                    return False
        if stack:
            print(False)
            return False
        print(stack)
        print(True)
        return True

res = Solution()
res.isValid("[")