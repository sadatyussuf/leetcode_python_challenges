# class Solution:
#     def isPalindrome(self, x: int) -> bool:

#         if x < 0:
#             return False
#         if str(x)[::-1] == str(x):
#             return True
# return False

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if (x < 0):
            return False
        reverse_x = 0
        temp_x = x
        while x > 0:
            reverse_x = (reverse_x * 10) + (x % 10)
            x = x // 10
        if reverse_x == temp_x:
            return True


test = Solution()
test.isPalindrome(0)
