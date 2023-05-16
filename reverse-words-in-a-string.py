class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        
        s = s.split()[::-1]

        for word in s:
            if word:
                res += " " + word
        return res.strip()