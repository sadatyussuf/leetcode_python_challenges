class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_s = s.split(' ')
        c = -1
        while True:
            if split_s[c] == '':
                print(split_s[c])

                c -=1
                print(c)
            else:
                return len(split_s[c])