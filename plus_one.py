class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        conv_str = ''.join(str(i) for i in digits)
        add_digits = int(conv_str) + 1

        res = [int(i) for i in str(add_digits)]

        return res